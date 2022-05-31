def generate_sql(table_name, col_names, constraints):
  """
  Is generating SQL codes to create new rows with types of datas
  """
  columns = [" ".join((col, constraint)).strip() for col, constraint in zip(col_names, constraints)]

  # łączy pojedyncze elementy z list dla petli for gdzie zippuje col + constraint w jednen tuple i wtedy joinuje

  return f'CREATE TABLE {table_name} (\n\t' + ',\n\t'.join(columns) + '\n)'
