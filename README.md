<h1>Project: Finance Manager</h1>

<h2>Project Description</h2>
<p>This project is a web application for managing finances, written in Django. The Finance Manager allows users to track income and expenses, categorizing them by relevant sources and categories. The main features include displaying the current balance, calculating income and expenses, monitoring the untouchable reserve (UR), sorting income and expenses, and ensuring the security of transactions.</p>

<h2>Functional Requirements</h2>
<p>The application implements the following functionality:</p>
<ul>
    <li><strong>Current Balance:</strong> Displays the user's current balance.</li>
    <li><strong>Untouchable Reserve (UR):</strong> A financial reserve that cannot be spent without additional confirmation.</li>
    <li><strong>Income Tracking:</strong> Displays the total income and a breakdown by income sources.</li>
    <li><strong>Expense Tracking:</strong> Displays the total expenses and a breakdown by expense categories.</li>
    <li><strong>CRUD:</strong> Create, read, update, and delete income|expenses.</li>
    <strong>❗️Editing and deleting income|expenses works incorrectly, as I haven't fully implemented budget recalculation after updates or deletions yet.❗️</strong>
    <li><strong>Graphical Interface:</strong> A user-friendly interface for managing income and expenses (even supports a console version).</li>
    <li><strong>Operation Control:</strong> If the current balance is less than or equal to the UR, the transaction is blocked. Users can override this restriction, but only after additional confirmation.</li>
    <li><strong>Income Sorting:</strong> From largest to smallest.</li>
    <li><strong>Expense Sorting:</strong> From smallest to largest.</li>
</ul>

<h2>Installation Requirements</h2>
<ul>
    <li>Python 3.9+</li>
    <li>Pip</li>
</ul>

<h2>Installation Instructions</h2>
<ol>
    <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/b7sj3o/finance_tracker_x-python.git</code></pre>
    </li>
    <li><strong>Navigate to the project directory:</strong>
        <pre><code>cd finance_tracker_x-python</code></pre>
    </li>
    <li><strong>Create a virtual environment (venv):</strong>
        <pre><code>python -m venv venv</code></pre>
    </li>
    <li><strong>Activate the venv:</strong>
        <pre><code>venv/Scripts/activate</code></pre> - if you are using Windows terminal
        <pre><code>source venv/bin/activate</code></pre> - if you are using Linux | MacOS
    </li>
    <li><strong>Install dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Enter the backend directory:</strong>
        <pre><code>cd backend</code></pre>
    </li>
    <li><strong>Setup the database:</strong>
        <p>Run migrations:</p>
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li><strong>Run the server:</strong>
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li><strong>Access the application:</strong>
        <p>Open your browser and go to <code>http://127.0.0.1:8000/</code>.</p>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Registration and Login:</strong>
        <p>Create an account and log in to the system.</p>
    </li>
    <li><strong>Add, Edit, and Delete Income:</strong>
        <p>Use the respective form to input new income data.</p>
    </li>
    <li><strong>Add, Edit, and Delete Expenses:</strong>
        <p>Enter expense details using the respective form.</p>
    </li>
    <li><strong>Finance Monitoring:</strong>
        <p>View current balance, income, and expenses in the respective menu sections.</p>
    </li>
    <li><strong>Change UR:</strong>
        <p>You can change the UR amount in the settings.</p>
    </li>
</ol>
