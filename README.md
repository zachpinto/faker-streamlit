# Faker Streamlit App

**A clean, interactive Streamlit GUI for the [Faker](https://github.com/joke2k/faker) library — generate fake datasets easily and export them as CSV.**

---

## Web App
Try a GUI version of Faker using the Streamlit web app: [Launch App](https://faker-streamlit.streamlit.app)

---

## Features

- ⚙️ Configure number of rows and columns
- 🧬 Per-column data type selection from Faker or manual format (e.g. `$###,###.##`)
- 🔁 Optionally restrict each field to a number of unique values
- 📄 Preview and download data as CSV
- 🧠 Uses the powerful [Faker](https://faker.readthedocs.io/) library for realistic fake data generation

---

## Screenshot

<img width="1470" alt="Screenshot 2025-05-04 at 1 03 12 PM" src="https://github.com/user-attachments/assets/255bafc1-a23f-45aa-a461-c836c0e97bb1" />

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/faker-streamlit.git
cd faker-streamlit
pip install -r requirements.txt
streamlit run app.py
```

## Requirements

- Python 3.8+
- Streamlit 1.45.0+
- Faker
- pandas

See [`requirements.txt`](./requirements.txt) for specific version constraints.

---

## About Faker

This app is built on top of the official [Faker](https://github.com/joke2k/faker) Python library.

Faker generates fake but realistic-looking data for a wide range of use cases, including:

- Personal identity: names, addresses, emails, phone numbers
- Internet and tech: usernames, IP addresses, domains, MACs
- Financial: credit cards, currencies, prices
- Location and datetime: cities, zip codes, datetimes
- Job and company info: job titles, employers, business jargon

Faker is especially useful for:
- Bootstrapping test databases
- Anonymizing production data
- Stress testing apps with large fake datasets

📚 Full docs here: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)

---

## Supported Formats

You can define fields in one of two ways:

### 1. **Faker Built-in Types (Dropdown)**
Choose from 100+ Faker methods, like:
- `name`, `address`, `email`, `company`, `job`
- `ipv4`, `iban`, `phone_number`, `credit_card_number`

Each row will call the selected method once to generate data for that column.

### 2. **Manual Pattern Format**
Use `#` for digits, `?` for uppercase letters, and include any literal characters you want.

**Examples**:
- `$###,###.##` → `$452,990.14`
- `??-####` → `AZ-9842`
- `Order-####-??` → `Order-1023-KL`

You can also limit each column to a fixed number of unique values (e.g. 10 departments, 50 zip codes).

---

## Example Use Cases

- Prototyping mock datasets for machine learning
- Populating UI components with realistic data
- Creating sample JSON APIs for demos
- Teaching data pipelines, visualization, or testing
- Filling out dashboards or Excel models quickly

---

## License


The underlying [Faker library](https://github.com/joke2k/faker/LICENSE) is also released under the MIT License.

---

## Acknowledgements

- Built with [Faker](https://github.com/joke2k/faker) by [@joke2k](https://github.com/joke2k)
- GUI powered by [Streamlit](https://streamlit.io/)
