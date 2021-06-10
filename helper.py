import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def loadData(path):

	df =  pd.read_csv(path)
	filtered_columns = ["Date", "Event-Name", "Full Name", "Fighter-2-Name", "W", "L", "D", "NC", "Finish-Time", "Finish-Round", "Total-Rounds", "Referee", "Fighter-Active-Status", "Height", "Weight", "Reach", "Stance", "Date of Birth"]
	df = df[filtered_columns]

	return df

def fightersList(df):
	return (df["Full Name"].unique())

def filteredData(df, name):
	df = df[df["Full Name"] == name]
	df.index = df["Date"]
	df = df.drop("Date", axis=1)
	return df

def plot(df):
	fig, ax = plt.subplots()
	ax.bar(["Win", "Lose", "Draw", "No-Contest"] ,[df[df["W"] == 1].shape[0], df[df["L"] == 1].shape[0], df[df["D"] == 1].shape[0], df[df["NC"] == 1].shape[0]], label="Count")
	plt.legend()
	plt.title("Record")
	plt.locator_params(integer=True)
	return fig