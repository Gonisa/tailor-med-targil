def get_cycle_days_number(df):
    df_columns = list(df.columns.values)
    if 'cycle_days_number' not in df_columns:
        if 'number_of_cycles' in df_columns and 'end_date' in df_columns and 'start_data' in df_columns:
            return (df['end_date'] - df['start_date']) / df['number_of_cycles']
