import random
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

def fetch_inflation_data(start_year, end_year):
    # Simulate real-time data by generating random inflation rates
    dates = []
    inflation_rates = []
    current_date = datetime(start_year, 1, 1)

    while current_date.year <= end_year:
        inflation_rate = random.uniform(-200, 800)  # Simulate inflation rate between -200% and 800%
        dates.append(current_date)
        inflation_rates.append(inflation_rate)
        current_date += timedelta(days=365 * 2)  # Increment by 2 years

    return dates, inflation_rates

def plot_inflation_data(dates, inflation_rates):
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(dates, inflation_rates, marker='o', linestyle='-')
    plt.title('Inflation Rate (Simulated Real-Time)')
    plt.xlabel('Year')
    plt.ylabel('Inflation Rate (%)')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.ylim(-200, 800)  # Set y-axis limits
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def main():
    start_year = 1987
    end_year = 2024

    dates, inflation_rates = fetch_inflation_data(start_year, end_year)

    # Plot the data
    plot_inflation_data(dates, inflation_rates)

if __name__ == "__main__":
    main()
