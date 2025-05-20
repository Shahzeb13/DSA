def compareDictionaries():

    freq1 = { "b" : 2 , "c" : 3}
    length = len(freq1);
    print(length);
    freq2 = { "c" : 3 , "b" : 2}
    matchFound= 0;
    for key1 in freq1:
        for key2 in freq2:
            print(f"Comparing {key1}:{freq1[key1]} with {key2}:{freq2[key2]}")
            if key1 == key2:
                print("✅Key Matched")
                if(freq1[key1] == freq2[key2]):
                    print("✅Value Matched")
                    print("✅ Match found!")
                    matchFound +=1;
                    print(f"Total Matches: {matchFound}")
                    
                if(freq1[key1] != freq2[key2]):
                    print("❌ Value mismatch!")
            
        print("❌Key Mismatched")
        continue
          
                

    if matchFound == len(freq1):
            return True;
    if matchFound != len(freq1):
            return False;
       
        

res = compareDictionaries()
print(res)
