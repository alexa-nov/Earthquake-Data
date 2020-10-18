from earthquake_funcs import *

last_sort = []
def main():
    print("Earthquakes:")
    print("------------")
    for quake in read_quakes_from_file("quakes.txt"):
        print(quake)
        last_sort.append(quake)
    print("\nOptions:")
    print("  (s)ort\n"," (f)ilter\n"," (n)ew quakes\n"," (q)uit\n")
    choice = input("Choice: ")
    while choice in "sSfFnNqQ":
        if choice in "sSFfnN":
            programming_options(choice)
            print("\nOptions:")
            print("  (s)ort\n"," (f)ilter\n"," (n)ew quakes\n"," (q)uit\n")
            choice = input("Choice: ")
        if choice in "qQ":
            programming_options(choice)
            break
        

def programming_options(choice):
    #Sort
    quakes = read_quakes_from_file("quakes.txt")
    if choice in "sS":
       last_sort.clear()
       sort_opt = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
       #Sort Magnitude
       if sort_opt in "mM":
          print("\nEarthquakes:")
          print("------------")
          for quake in sort_by_mag(quakes):
             print (quake)
             last_sort.append(quake)
       #Sort Time
       elif sort_opt in "tT":
          print("\nEarthquakes:")
          print("------------")
          for quake in sort_by_time(quakes):
             print (quake)
             last_sort.append(quake)
       #Sort Longitude
       elif sort_opt in "lL":
          print("\nEarthquakes:")
          print("------------")
          for quake in sort_by_longitude(quakes):
             print (quake)
             last_sort.append(quake)
       #Sort Latitude
       elif sort_opt in "aA":
          print("\nEarthquakes:")
          print("------------")
          for quake in sort_by_latitude(quakes):
             print (quake)
             last_sort.append(quake)
    #Filter
    elif choice in "fF":
       filter_opt = input("Filter by (m)agnitude or (p)lace? ")
       #Filter Place
       if filter_opt in "pP":
          string_input = input("Search for what string? ")
          print("\nEarthquakes:")
          print("------------")
          for quake in filter_by_place(last_sort, string_input):
             print (quake)
       #Filter Magnitude
       elif filter_opt in "mM":
          mag_low = float(input("Lower bound: "))
          mag_high = float(input("Upper bound: "))
          print("\nEarthquakes:")
          print("------------")
          for quake in filter_by_mag(last_sort, mag_low, mag_high):
             print (quake)
    #New Quakes
    elif choice in "nN":
       quakes_data = get_json("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson")
       feature = quakes_data["features"]
       print("\nEarthquakes:")
       print("------------")
       for quake in quake_from_feature(feature):
          print (quake)
          last_sort.append(quake)
       for quake in read_quakes_from_file("quakes.txt"):
          print (quake)
          last_sort.append(quake)
       for quake in quake_from_feature(feature):
          if quake not in read_quakes_from_file("quakes.txt"):
              print("\nNew quakes found!")
              break           
    #Quit
    elif choice in "qQ":
        outFile = open("quakes.txt", "w")
        for quake in last_sort:
            outFile.write("%s %s %s %s %s" %(quake.mag, quake.longitude, quake.latitude, quake.time, quake.place))
            outFile.write("\n")
        outFile.close()


if __name__ == '__main__':
    main()
