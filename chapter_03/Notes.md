# Six Stages of Development

## A Unit Converter App

### 1. **State the concept:**

**CONCEPT:**

-   A Streamlit app that allows users to effortlessly convert between different units of
    measurement, such as distance, mass, and time.

### 2. **Define Requirements**

**REQUIREMENTS:**

-   The user should be able to enter a numeric quantity and the unit in which
    the quantity is expressed (the "from-unit").
-   The user should be able to select a unit to convert to (the "to-unit"),
    which must measure the same type of thing as the from-unit. No
    converting from pounds to yards, for instance.
-   The app should display the converted value as output.
-   The app should be able to handle conversions within both imperial and
    metric systems (e.g., feet to inches or meters to centimeters), as well as
    conversions across systems (e.g., feet to meters).
-   Adding new units or quantities to the app should be straightforward.

**WHAT'S OUT OF SCOPE**

-   Usage tracking, logging, visualizations, etc., that do not directly relate to
    unit conversion
-   Conversions between units that don't share a simple, constant conversion
    factor, such as those between currencies.

### 3. Visualizing The User Experience

**Creating a Mock**

-   Provide a way for users to input a numeric value and the units to convert
    from and to (which must both measure the same type of quantity).
-   Output the converted value

### 4. Brainstorming the implementation

There are two primary components to most applications: a frontend and a backend. The
frontend handles how users interact with your app, i.e., how we collect inputs and display
outputs. The backend is the app's "brain," which takes inputs from the frontend, processes
them, and hands the output back to the frontend to display to the user.

**Mapping the Flow of Logic**

Once we have a good understanding of our app's pieces: the frontend, the program's logic, and the configuration. Before we code them up, having a mental model of how they fit together is useful.

### 5. Writing Code

At this point, we've spent enough time thinking about the design of our app that we're
ready to write some code.
