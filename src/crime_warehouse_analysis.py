import matplotlib.pyplot as plt
import seaborn as sns
from supabase_connection import fetch_table


def load_views():
    monthly_trends = fetch_table("vw_monthly_crime_trends")
    top_towns = fetch_table("vw_top_high_severity_towns")
    peak_hour = fetch_table("vw_peak_hour_crimes")
    return monthly_trends, top_towns, peak_hour


def plot_monthly_trends(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df,
        x="month",
        y="crime_count",
        hue="severity",
        marker="o"
    )
    plt.title("Monthly Crime Trends by Severity")
    plt.tight_layout()
    plt.show()


def plot_top_towns(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df,
        x="crime_count",
        y="town"
    )
    plt.title("Top Towns by High-Severity Crimes")
    plt.tight_layout()
    plt.show()


def plot_peak_hour(df):
    plt.figure(figsize=(5, 4))
    sns.barplot(
        data=df,
        x="is_peak_hour",
        y="crime_count"
    )
    plt.title("Peak vs Non-Peak Hour Crimes")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    monthly, towns, peak = load_views()
    plot_monthly_trends(monthly)
    plot_top_towns(towns)
    plot_peak_hour(peak)
