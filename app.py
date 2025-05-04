import streamlit as st
import pandas as pd
import random
from faker import Faker
import inspect

st.set_page_config(page_title="Fake Data Generator", layout="wide")
st.title("📊 Fake Data Generator using Faker")

st.sidebar.header("Dataset Settings")
num_rows = st.sidebar.number_input("Number of rows", min_value=1, max_value=100_000, value=100)
num_fields = st.sidebar.number_input("Number of fields", min_value=1, max_value=20, value=5)
use_weighting = st.sidebar.checkbox("Use real-world frequency weighting", value=True)

# Initialize Faker
fake = Faker(use_weighting=use_weighting)


# Helper to list valid faker methods
def get_faker_methods():
    blacklist = {
        "random", "add_provider", "seed", "seed_instance", "unique", "random_element",
        "lexify", "bothify", "numerify", "binary", "profile", "simple_profile", "random_choices"
    }

    safe_methods = []
    for attr in dir(fake):
        if attr.startswith("_") or attr in blacklist:
            continue
        try:
            method = getattr(fake, attr)
            if callable(method):
                safe_methods.append(attr)
        except TypeError:
            continue  # Skip methods that raise TypeError (like .seed)
    return sorted(safe_methods)



faker_methods = get_faker_methods()

# Section: Field Configs
st.subheader("Define Fields")
st.markdown(
    "Choose a data type from Faker *or* manually enter a format (e.g., `$#,###.##`).")

st.markdown("You can also choose how many unique values are generated per field.")

field_configs = []
for i in range(num_fields):
    with st.expander(f"Field {i + 1}", expanded=True):
        col1, col2 = st.columns([2, 3])

        with col1:
            field_name = st.text_input(f"Field name", value=f"field_{i + 1}", key=f"field_name_{i}")

        dtype_mode = st.radio(
            f"Data type source", ["Choose from Faker", "Manual entry format"],
            key=f"datatype_mode_{i}", horizontal=True
        )

        if dtype_mode == "Choose from Faker":
            faker_type = st.selectbox("Faker type", options=faker_methods, key=f"faker_type_{i}")
            manual_format = None
        else:
            faker_type = None
            manual_format = st.text_input("Custom format (e.g., $###,###.##)", key=f"manual_format_{i}")

        unique_values = st.number_input(
            "Limit to N unique values (optional)",
            min_value=0, max_value=num_rows, value=0, key=f"unique_{i}"
        )

        field_configs.append({
            "name": field_name,
            "faker_type": faker_type,
            "manual_format": manual_format,
            "unique_n": unique_values if unique_values > 0 else None,
        })

# Generate data
if st.button("Generate Data"):
    data = {}
    for config in field_configs:
        col_name = config["name"]
        n_unique = config["unique_n"]

        if config["manual_format"]:
            fmt = config["manual_format"]
            samples = []
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            digits = "0123456789"


            def render_format():
                output = ""
                for ch in fmt:
                    if ch == "#":
                        output += random.choice(digits)
                    elif ch == "?":
                        output += random.choice(chars)
                    else:
                        output += ch
                return output


            if n_unique:
                values = [render_format() for _ in range(n_unique)]
                data[col_name] = [random.choice(values) for _ in range(num_rows)]
            else:
                data[col_name] = [render_format() for _ in range(num_rows)]

        elif config["faker_type"]:
            faker_fn = getattr(fake, config["faker_type"])
            if n_unique:
                try:
                    values = list({faker_fn() for _ in range(n_unique * 3)})[:n_unique]
                except Exception as e:
                    st.error(f"Error creating unique values for {col_name}: {e}")
                    continue
                data[col_name] = [random.choice(values) for _ in range(num_rows)]
            else:
                try:
                    data[col_name] = [faker_fn() for _ in range(num_rows)]
                except Exception as e:
                    st.error(f"Error generating {col_name}: {e}")
                    continue
        else:
            st.error(f"Invalid configuration for field: {col_name}")
            continue

    df = pd.DataFrame(data)
    st.success("✅ Data generated!")
    st.dataframe(df.head(20), use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, file_name="fake_data.csv", mime="text/csv")
