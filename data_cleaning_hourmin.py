import pandas as pd 

def appointmets_clean(input_file):
    df = pd.read_csv(input_file)
    df["Hour_Min"] = df["Appointment duration (actual)"].str.split(" ")
    df.dropna(subset = ["Appointment duration (actual)"], inplace = True)

    print(df[df["Appointment duration (actual)"].isna()])

    mins_per_unit = {"m": 1, "h": 60}

    def convert_to_mins(hour_min):
        if len(hour_min) < 1:
            times = 0
        else:
            times = [(int(x[:-1]) * mins_per_unit[x[-1]]) for x in hour_min]
        return sum(times)

    df["Duration"] = df["Hour_Min"].apply(convert_to_mins)
    df.drop(['Hour_Min'], axis=1)
    return df