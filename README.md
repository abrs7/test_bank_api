# Django REST API with Docker - Bank API

This project is a Django REST API that provides endpoints for handling bank and branch data, as well as submitting applications. The application is containerized using Docker for easy deployment.

##  Features
- **Get List of Banks** (`GET /api/banks`)
- **Get Branches by Bank** (`GET /api/branches?bank_id={id}`)
- **Submit an Application** (`POST /api/applications/submit`)

---

## 🛠️ Setup Instructions
- **User a virtual environment** (`python3 -m venv venv`)
- **Inter into the virtual environment** (`source venv/bin/activate`)

### Step 1: Clone the Repository
```sh
git clone https://github.com/abrs7/test_bank_api.git
cd test_bank_api
```

### 2️⃣ Install Dependencies (Optional - If Running Locally)
```sh
pip install -r requirements.txt
```

### 3️⃣ Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Start the Server (Local Mode)
```sh
python manage.py runserver 0.0.0.0:8000
```

The API will be available at **http://localhost:8000**

---

## 🐳 Running with Docker

### 1️⃣ Build the Docker Image
```sh
docker build -t bank_api_image .
```

### 2️⃣ Run the Docker Container
```sh
docker run -p 8000:8000 bank_api_image
```

Now, visit **http://localhost:8000** to access the API.

---

## 📖 API Documentation

### 1️⃣ Get Banks
**Endpoint:** `GET /api/banks`
```json
{
  "banks": [
    { "id": 1, "value": "Bank A" },
    { "id": 2, "value": "Bank B" }
  ]
}
```

### 2️⃣ Get Branches
**Endpoint:** `GET /api/branches?bank_id={id}`
```json
{
  "branches": [
    { "id": 1, "value": "Branch X" },
    { "id": 2, "value": "Branch Y" }
  ]
}
```

### 3️⃣ Submit an Application
**Endpoint:** `POST /api/applications/submit`

**Request Body:**
```json
{
  "bank_name": "Bank A",
  "branch_name": "Branch X",
  "account_name": "John Doe",
  "account_number": "123456789"
}
```

**Response:**
```json
{
  "message": "Application submitted successfully",
  "id": 1
}
```

---

## 📌 Notes
- Ensure that Docker is installed if running with Docker.


---

## 🏆 Contributors
- **Abraham Asrat** (abrahamasrat791@gmail.com)

---

