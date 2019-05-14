def extract_data(filename):
    _sum = 0
    count = 0
    with open(filename, "r") as file:
        for line in file:
            if "t_map.add_point_cartesian(point, PointState.occupied)" in line:
                new_line = line[8:15]           # Get the memory usage
                _sum += float(new_line)
                count += 1

            elif "<===" in line:
                name = line[4:-1]               # Map identification
                file.readline()                 # Skip blank line
                time = file.readline()[:-1]     # Grab the time until newline
                print("Name:\t\t\t", name)
                print("Sample count:\t", count)
                print("Time:\t\t\t", time, "s")
                print("Average:\t\t", (_sum / count), "MiB\n")
                _sum = 0                        # Reset values for next map
                count = 0
    file.close()
