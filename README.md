# Web-crawling

How to use?

  downloadcssimages.py: Download images from css files of websites.
  
    Python 2: python downloadcssimages.py <site-name>
  
    Python 3: python3 downloadcssimages.py <site-name>
  
    e.g.
      
      python downloadcssimages.py http://www.imdb.com/
  
    NOTE:
      base64 images will give an error.
  
  moviescript.py: Save movie name, rating and director name of movies, with ratings>=6.5 and <=8.5 in a CSV file, from imdb. A link of a movie has to be provided as argument and the subsequent movies are picked up from "People who liked this also liked..." section. 
  
    Python 2: python moviescript.py <movie-link-from-imdb> <no-of-movies-to-fetch>
  
    Python 3: python3 moviescript.py <movie-link-from-imdb> <no-of-movies-to-fetch>
  
    e.g.
      
      python moviescript.py http://www.imdb.com/title/tt0337978/ 10
  
    NOTE:
      Ratings can be customized. 
      The list will be saved in a CSV file named new.csv. 
      The CSV file will be overwritten if the script is run again with new arguments
    
