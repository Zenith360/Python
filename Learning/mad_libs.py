def shut_down(s):
    if(shut_down(s) == "yes"):
        return "shutting down!";
    elif(shut_down(s) == "no"):
        return "shutdown aborted"
    else:
        return "sorry";
shut_down("yes");