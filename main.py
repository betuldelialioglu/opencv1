import cv2
path = input()
control1 = False
control2 = False
img = cv2.imread(path, -1)
img = cv2.resize(img, (800, 800))

def click_event(event,x,y,flags,param):
    global pt1
    global control1
    global x1, y1
    global pt2
    global control2
    global x2, y2

    if event == cv2.EVENT_RBUTTONDOWN and not(flags & cv2.EVENT_FLAG_CTRLKEY) and not(flags & cv2.EVENT_FLAG_ALTKEY):

        img2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("image", img2)
    elif event == cv2.EVENT_LBUTTONDOWN and not(flags & cv2.EVENT_FLAG_CTRLKEY) and not(flags & cv2.EVENT_FLAG_ALTKEY):

        img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("image", img2)
    if event==cv2.EVENT_LBUTTONDOWN and flags & cv2.EVENT_FLAG_CTRLKEY:
        pt1 = (x,y)
        x1, y1 = x, y
        control1 = True
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_CTRLKEY and control1:
        img_copy = img.copy()
        cv2.rectangle(img_copy, pt1, (x,y), (0, 255, 0), 1)
        cv2.imshow("image", img_copy)
    elif event == cv2.EVENT_LBUTTONUP and flags & cv2.EVENT_FLAG_CTRLKEY and control1:
        control1 = False
        cv2.rectangle(img, pt1, (x,y), (0, 255, 0), 1)
        cv2.imshow("image", img)
        cropped_img = img[min(y1, y): max(y1, y), min(x1, x): max(x1, x)]
        cv2.imwrite("cropped_image.jpg", cropped_img)
    elif event == cv2.EVENT_LBUTTONDOWN and flags & cv2.EVENT_FLAG_ALTKEY:
        cv2.putText(img, "Betul", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (int(img[y,x,0]), int(img[y,x,1]), int(img[y,x,2])), 2)
        cv2.imshow("image", img)
    elif event == cv2.EVENT_RBUTTONDOWN and flags & cv2.EVENT_FLAG_CTRLKEY:
        pt2 = (x, y)
        x2, y2 = x, y
        control2 = True
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_CTRLKEY and control2:
        img_copy2 = img.copy()
        cv2.circle(img_copy2, pt2, int(((x2 - x) ** 2 + (y2 - y) ** 2) ** (1 / 2)), (0, 0, 255), -1)
        cv2.imshow("image", img_copy2)
    if event == cv2.EVENT_RBUTTONUP and flags == cv2.EVENT_FLAG_CTRLKEY:
        control2 = False
        cv2.circle(img, pt2, int(((x2 - x) ** 2 + (y2 - y) ** 2) ** (1 / 2)), (0, 0, 255), -1)
        cv2.imshow("image", img)

    elif event == cv2.EVENT_RBUTTONDOWN and flags & cv2.EVENT_FLAG_ALTKEY:
        cv2.imwrite("edited_img.jpg", img)
cv2.imshow("image", img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()