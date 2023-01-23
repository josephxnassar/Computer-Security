from hashlib import md5

def most_frequent(testList):
        max_num_occur = 0
        valu = -1
     
        for item in testList:
            cur_occur = testList.count(item)
            if cur_occur > max_num_occur:
                max_num_occur = cur_occur
                value = item
 
        return value

def read_file(input_file):
    with open(input_file, "r") as infile:
        fileList = infile.readlines()

    uid = list()
    gid = list()
    uname = list()
    email = list()
    pwd = list()
    auth = list()
    failedlogin = list()

    for line in fileList:
        lineAsList = line.split(sep = ",")
        uid.append(int(lineAsList[0]))
        gid.append(int(lineAsList[1]))
        uname.append(lineAsList[2])
        email.append(lineAsList[3])
        pwd.append(lineAsList[4])
        auth.append(lineAsList[5])
        failedlogin.append(int(lineAsList[6]))
    
    infile.close()

    return uid, gid, uname, email, pwd, auth, failedlogin

def get_md5_ciphertext(text):
    md5_hash = md5()
    md5_hash.update(text.encode('utf-8'))

    # md5_hash.update(b'hello') also works but not when string is in a var

    return md5_hash.hexdigest()

def main():
    
    uid1, gid1, uname1, email1, pwd1, auth1, failedlogin1 = read_file("password1.txt")
    uid2, gid2, uname2, email2, pwd2, auth2, failedlogin2 = read_file("password2.txt")

    with open("wordList.txt", "r") as wordfile:
        wordList = wordfile.read().splitlines()
    
        # done like this to remove \n

    # num entries (1)
    print("Length of file pwd1.txt: {length}".format(length=len(uid1)))

    # most freq pwd (2)
    print("Most frequent password in pwd1.txt {freq}".format(freq=most_frequent(pwd1)))

    # most failed login attempts (3)
    max_fail = max(failedlogin1)
    max_user = failedlogin1.index(max_fail)

    print("Max number of failed attempts: {max}. Index of user: {index}. User ID: {uid}".format(max=max_fail,index=max_user,uid=uid1.__getitem__(max_user)))

    # -=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=

    # Finding secret salt word (4)

    key = str()

    for word in wordList:
        for salt in wordList:
            if get_md5_ciphertext(word+salt) in pwd2:
                key = salt
                break

    print(f"Secret salt word is {key}")

    # key revealed to be selective (takes roughly 10 minutes)

    # -=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=

    count = 0

    for word in wordList:
        if get_md5_ciphertext(word+"selective") in pwd2:
            count += 1

    # should be (around) 621
    print(f"Number of pwds in pwd2.txt with salt as selective {count}")

    # Everything below this is not important!!!

    # -=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=

    # Test Case 1

    # hidden = str()

    # for word in wordList:
    #     for salt in wordList:
    #         if get_md5_ciphertext(word+salt) == "d41d8cd98f00b204e9800998ecf8427e":
    #             hidden = word + " " + salt
    #             print(f"Test Case 1 Passed: Secret word+salt is {hidden}")
    #             break
    # if hidden == "":
    #     print("Test Case 1 Failed")

    # should print out a word but doesn't (test case is broken)

    # Test Case 2

    secret = str()

    # for salt in wordList:
    #     if get_md5_ciphertext("abandoned"+salt) == "81f3d2a447d9c5579b446ff048827de1":
    #         secret = salt
    #         print(f"Test Case 2 Passed: Secret salt word is {salt}")
    #         break
    # if secret == "":
    #     print("Test Case 2 Failed")

    # should print out a word but doesn't (test case is broken)

    # -=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=

    # Test Case 3
    
    # if get_md5_ciphertext("idahosaturn") == "81d4ce3fd1613924ed42bb4928c7e645":
    #     print("Test Case 3 passed")
    # else:
    #     print("Test Case 3 failed")

    # for salt in wordList:
    #     if get_md5_ciphertext("idaho"+salt) == "81d4ce3fd1613924ed42bb4928c7e645":
    #         print(f"Test case 3 works {salt}")
    # # expected result is saturn, and when run, program gives saturn

    # -=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=

    # Proof my md5 works and test cases are just messed up

    # if get_md5_ciphertext("hello") == "5d41402abc4b2a76b9719d911017c592":
    #     print("Hello cipher works")

    # if get_md5_ciphertext("hellothere") == "c6f7c372641dd25e0fddf0215375561f":
    #     print("Hellothere cipher works")

    # if get_md5_ciphertext("helloworld") == "fc5e038d38a57032085441e7fe7010b0":
    #     print("Helloworld cipher works")

if __name__ == "__main__":
    main()