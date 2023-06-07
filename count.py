import subprocess;

while True:
  try:
    numberIni = int(input("Enter a Integer Number Initial: "))
    numberEnd = int(input("Enter a Integer Number End: "))
    if numberEnd < numberIni:
      print("[+] The start number must be less than the end number.")
    else:
      print("[+] Perfect.")
    break;
  except:
    print("[+] ¡ENTER A INTEGER NUMBER!")

def increment_number(numIni, numEnd):
  for num in range(numIni, numEnd):
    if num == numIni:
      num + 1;
      command1 = "touch totalCount.txt";
      command2 = f"echo {num} >> totalCount.txt";
      proceso1 = subprocess.Popen(command1, shell=True);
      proceso1.wait();
      proceso2 = subprocess.Popen(command2, shell=True);
      proceso1.wait();
    elif num < numEnd:
      num + 1;
      command1 = "touch totalCount.txt";
      command2 = f"echo {num} >> totalCount.txt";
      proceso1 = subprocess.Popen(command1, shell=True);
      proceso1.wait();
      proceso2 = subprocess.Popen(command2, shell=True);
      proceso1.wait();
    else:
      print(f"[+] Number end is {num}")

increment_number(numberIni, numberEnd+1)


print("[+] Open totalCount.txt")