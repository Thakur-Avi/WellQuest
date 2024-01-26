# WellQuest: Your Ultimate Fitness and Wellness Companion

Welcome to WellQuest, your go-to web application for a holistic fitness and wellness experience! Our beautifully designed landing page invites you into a world of motivation and health. Discover redirect links to YouTube channels of renowned fitness mentors and coaches, providing you with expert guidance and inspiration. Immerse yourself in motivating messages and quotes to fuel your fitness journey.

The landing page doesn't just stop at inspiration; it also helps you navigate your health environment. Utilize the integrated map feature to explore hospitals nearby your location, ensuring your health is always a priority.

### Feature Highlights:

**1. YouTube Fitness Hub:**
   - Dive into a handpicked selection of YouTube channels featuring renowned fitness mentors and coaches. Elevate your workouts with expert guidance, ensuring each session is a step towards your peak fitness.

**2. Motivational Quotes:**
   - Ignite your inner drive with our curated collection of motivational messages and quotes. Each phrase is a beacon of inspiration, fueling your commitment to a healthier, happier you.

**3. Hospital Locator:**
   - Navigate your health landscape effortlessly with our interactive map feature. Discover nearby hospitals, ensuring that quality healthcare is always within reach. Your well-being is our priority.

### Additional Enhancements:

- **Calorie Counter:**
  - Make informed dietary decisions with our intuitive calorie counter. Easily calculate the nutritional value of your food, supporting your journey to a balanced lifestyle.

- **Mental Health Oasis:**
  - Find solace in our dedicated space for mental health resources. WellQuest is committed to supporting your mental wellness, recognizing the integral role it plays in your overall health.

- **Fitness Indices Calculator:**
  - Gauge your fitness progress with precision using our advanced fitness indices calculator. Track your achievements and set new milestones on your wellness expedition.

- **Muscle-Specific Exercises:**
  - Receive personalized exercise recommendations targeting specific muscle groups. Tailor your fitness routine to achieve a harmonious and well-rounded physique.

### Prerequisites for WellQuest:

1. **Python:**
   - WellQuest is a Python-based web application, so it is essential to have Python installed on your system. Download the latest version of Python from its official website: [Python Downloads](https://www.python.org/downloads/).

2. **Virtual Environment:**
   - A virtual environment helps manage project-specific dependencies. Install 'virtualenv' by entering the following command in your terminal:
     ```
     pip install virtualenv
     ```
     Once installed, you can create a virtual environment using:
     - On Windows:
       ```
       python -m venv env
       ```
     - On macOS/Linux:
       ```
       python3 -m venv env
       ```

### Steps for Virtual Environment Setup:

   - **Activate the Virtual Environment:**
     - On Windows:
       ```
       .\env\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source env/bin/activate
       ```

### Note:
   - Ensure that the virtual environment is activated before proceeding with the WellQuest setup steps.

## How to Embark on Your WellQuest Journey:

Clone this repository, follow our straightforward setup instructions, and embark on a wellness journey that transcends expectations. WellQuest is not just an application; it's a companion dedicated to sculpting a healthier, more vibrant version of you.

To effortlessly set up and run WellQuest on your local environment, follow these simple steps:

### 1. Navigate to Scripts in the `env` folder:
   - Open the `env` folder associated with your WellQuest project.
   - Locate the `Scripts` folder within it.

### 2. Open Command Prompt in this directory:
   - Right-click inside the `Scripts` folder.
   - Select "Open Command Prompt Here."

### 3. Activate the Virtual Environment:
   - Type the 'Activate' command and press Enter.
     ```
     activate
     ```
   - This will initialize the virtual environment, ensuring a clean and isolated workspace.

### 4. Navigate Back to the Main Directory:
   - Use the 'cd ..' command to return to the directory containing the `env` folder.

### 5. Install dependencies from requirements.txt:
   - Type the command in terminal and press enter.
     ```
     pip install -r requirements.txt
     ```

### 6. Enter the WellQuest Directory:
   - Move to the WellQuest directory using the 'cd wellQuest' command in the terminal.

### 7. Start the WellQuest Server:
   - Type 'python manage.py runserver' in the terminal and press Enter.
     ```
     python manage.py runserver
     ```
   - The server will start, and you can access WellQuest locally at `localhost:8000`.

### 7. Quit the Server:
   - To stop the server, navigate to the command prompt and press 'Ctrl+C.'
