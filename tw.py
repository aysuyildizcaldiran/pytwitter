import twint
c = twint.Config()
c.Search="apple"
c.Store_csv=True
c.Output="custom.csv"
twint.run.Search(c)

