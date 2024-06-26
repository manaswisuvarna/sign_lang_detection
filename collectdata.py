
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/a")),
             'b': len(os.listdir(directory+"/b")),
             'c': len(os.listdir(directory+"/c")),
            #  'd': len(os.listdir(directory+"/D")),
             'e': len(os.listdir(directory+"/eat")),
            #  'f': len(os.listdir(directory+"/F")),
             'g': len(os.listdir(directory+"/g")),
             'h': len(os.listdir(directory+"/hello")),
             'i': len(os.listdir(directory+"/iloveyou")),
            #  'j': len(os.listdir(directory+"/J")),
             'k': len(os.listdir(directory+"/k")),
             'l': len(os.listdir(directory+"/l")),
            #  'm': len(os.listdir(directory+"/M")),
             'n': len(os.listdir(directory+"/no")),
             'o': len(os.listdir(directory+"/ok")),
            #  'p': len(os.listdir(directory+"/P")),
            #  'q': len(os.listdir(directory+"/Q")),
            #  'r': len(os.listdir(directory+"/R")),
            #  's': len(os.listdir(directory+"/S")),
             't': len(os.listdir(directory+"/thankyou")),
            #  'u': len(os.listdir(directory+"/U")),
             'v': len(os.listdir(directory+"/where")),
             'w': len(os.listdir(directory+"/water")),
            #  'x': len(os.listdir(directory+"/X")),
             'y': len(os.listdir(directory+"/yes")),
            #  'z': len(os.listdir(directory+"/Z"))
             }
    # cv2.putText(frame, "a : "+str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "b : "+str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "c : "+str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "d : "+str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "e : "+str(count['e']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "f : "+str(count['f']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "g : "+str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "h : "+str(count['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "i : "+str(count['i']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "k : "+str(count['k']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "l : "+str(count['l']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "m : "+str(count['m']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "n : "+str(count['n']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "o : "+str(count['o']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "p : "+str(count['p']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "q : "+str(count['q']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "r : "+str(count['r']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "s : "+str(count['s']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "t : "+str(count['t']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "u : "+str(count['u']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "v : "+str(count['v']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "w : "+str(count['w']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "x : "+str(count['x']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "y : "+str(count['y']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "z : "+str(count['z']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'a/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'b/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'c/'+str(count['c'])+'.png',frame)
    # if interrupt & 0xFF == ord('d'):
    #     cv2.imwrite(directory+'D/'+str(count['d'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'eat/'+str(count['e'])+'.png',frame)
    # if interrupt & 0xFF == ord('f'):
    #     cv2.imwrite(directory+'F/'+str(count['f'])+'.png',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'g/'+str(count['g'])+'.png',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'hello/'+str(count['h'])+'.png',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'iloveyou/'+str(count['i'])+'.png',frame)
    # if interrupt & 0xFF == ord('j'):
    #     cv2.imwrite(directory+'J/'+str(count['j'])+'.png',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'k/'+str(count['k'])+'.png',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'l/'+str(count['l'])+'.png',frame)
    # if interrupt & 0xFF == ord('m'):
    #     cv2.imwrite(directory+'M/'+str(count['m'])+'.png',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'no/'+str(count['n'])+'.png',frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'ok/'+str(count['o'])+'.png',frame)
    # if interrupt & 0xFF == ord('p'):
    #     cv2.imwrite(directory+'P/'+str(count['p'])+'.png',frame)
    # if interrupt & 0xFF == ord('q'):
    #     cv2.imwrite(directory+'Q/'+str(count['q'])+'.png',frame)
    # if interrupt & 0xFF == ord('r'):
    #     cv2.imwrite(directory+'R/'+str(count['r'])+'.png',frame)
    # if interrupt & 0xFF == ord('s'):
    #     cv2.imwrite(directory+'S/'+str(count['s'])+'.png',frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'thankyou/'+str(count['t'])+'.png',frame)
    # if interrupt & 0xFF == ord('u'):
    #     cv2.imwrite(directory+'U/'+str(count['u'])+'.png',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'where/'+str(count['v'])+'.png',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'water/'+str(count['w'])+'.png',frame)
    # if interrupt & 0xFF == ord('x'):
    #     cv2.imwrite(directory+'X/'+str(count['x'])+'.png',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'yes/'+str(count['y'])+'.png',frame)
    # if interrupt & 0xFF == ord('z'):
    #     cv2.imwrite(directory+'Z/'+str(count['z'])+'.png',frame)


cap.release()
cv2.destroyAllWindows()