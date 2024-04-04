import matplotlib

# Set the backend to Agg before importing pyplot
matplotlib.use('Agg')
import matplotlib.pyplot as plt


from flask import Flask, render_template, Response
import numpy as np
import csv
import time

app = Flask(__name__)

# Initialize CSV file with header if it doesn't exist
csv_file = "random_values_conti1.csv"
with open(csv_file, 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['X', 'Y'])  # Write header

# Route to the main page
@app.route('/')
def index():
    return render_template('index.html')

# Generator function to continuously generate random data
def generate_random_data():
    while True:
        # Generate data
        x = np.linspace(0, 10, 100)  # Range from 0 to 10
        y = np.random.uniform(-2, 2, 100)  # Random numbers between -2 and 2

        # Append new data to CSV file
        with open(csv_file, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for i in range(len(x)):
                csv_writer.writerow([x[i], y[i]])  # Write new data

        # Read all data from CSV file
        with open(csv_file, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip header row
            data = list(csv_reader)

        # Convert data to numpy array
        data_to_plot = np.array(data[-100:], dtype=float)

        # Initialize plot
        # Initialize plot
        fig, ax = plt.subplots(figsize=(12.4, 4.07))
        ax.plot(data_to_plot[:, 0], np.sin(data_to_plot[:, 1]))  # Add label to the plot
        ax.set_title('Visualization of Data from CSV')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.grid(True)


        # Save the plot as an image
        plt.savefig('static/plot.png')

        # Close the plot to release resources
        plt.close()

        # Yield the image data
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + open('static/plot.png', 'rb').read() + b'\r\n')

        # Wait for a certain duration before generating new data (e.g., 1 second)
        time.sleep(0.00001)


# Route to stream the generated plot as an image
@app.route('/plot.png')
def plot_png():
    return Response(generate_random_data(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
