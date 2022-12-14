
def count_batteries_by_usage(cycles):
  lowCount=0
  mediumCount=0
  highCount=0
  
  for i in range(len(cycles)):
        if cycles[i]<400:
            lowCount=lowCount+1
        if 400<=cycles[i] and cycles[i]<=919:
            mediumCount=mediumCount+1
        if cycles[i]>=920:
            highCount=highCount+1
            #return the values in the form of a list
  return {
    "lowCount": lowCount,
    "mediumCount": mediumCount,
    "highCount": highCount
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  #testing for the above mentioned case
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")
  print(counts)


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
