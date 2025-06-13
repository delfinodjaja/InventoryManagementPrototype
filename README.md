<h2>Features</h2>

<ul>
  <li><strong>Role-based access:</strong> Users can be <code>Staff</code>, <code>Customer</code>, or <code>Doctor</code>.</li>
  <li><strong>Doctor-specific view:</strong> Doctors can view <em>only their own appointments</em>.</li>
  <li><strong>Admin control:</strong> Admin can manage roles and users via the <code>/admin</code> panel.</li>
  <li><strong>Inventory system:</strong> Simple inventory with full <strong>CRUD</strong> (Create, Read, Update, Delete) functionality.</li>
  <li><strong>Web interface:</strong> All core actions are performed through the built-in web interface.</li>
</ul>
<h2>How to Use</h2>
<li>First, clone the repository using git clone, then navigate into the project folder.</li>

<li>Create a virtual environment using python -m venv venv, and activate it. On Windows, use venv\Scripts\activate; on macOS/Linux, use source venv/bin/activate.</li>

<li>Install all required dependencies by running pip install -r requirements.txt.</li>

<li>Apply the migrations by running python manage.py migrate.</li>

<li>Create a superuser account with python manage.py createsuperuser and follow the prompts.</li>

<li>Start the development server using python manage.py runserver.</li>

<li>Open your browser and go to http://127.0.0.1:8000/ to view the project.</li>
