# import glassdoor_scrapper as gs
import glassdoor_scraping as gs
import pandas as pd

path='/home/ermi/Desktop/Datascience/scripts/chromedriver'

df = gs.get_jobs('data scientist','Ethiopia',1,'false', path,15)
