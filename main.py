import cv2

cap = cv2.VideoCapture(0)

chars = (".", ":", "!","/","r", "(","l","Z","4","H","9","W","8","$","@")
if not cap.isOpened():
    raise RuntimeError("Не удалось открыть камеру")
CLEAR = "\033[2J\033[H"
while True:
    ok, frame = cap.read()
    if not ok:
        print("Не удалось прочитать кадр")
        break
    frame = cv2.resize(frame, (320, 140)) # ЗДЕСЬ СНАЧАЛА ПИШЕТСЯ ШИРИНА БЛ*** А ПОТОМ ВЫСОТА, в шейпе СНАЧАЛА ИДЕТ ВЫСОТА ПОТОМ ШИРИНА

    w = frame.shape[1]  #320
    h = frame.shape[0]  #140




    lines = []

    cv2.imshow("Camera", frame)
    for i in range(h):
        line = []
        for j in range(w):
            #col = frame[i][j]
            color = (frame[i][j][0] + frame[i][j][1] + frame[i][j][2])/3
            char = chars[int(color/16)]
            line.append(char)

        lines.append("".join(line))

    # for l in lines:
    #     print(l, flush=True)
    print("\033[2J\033[H", flush=True)
    res = "\n".join(lines)
    print(res, flush=True)



    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
