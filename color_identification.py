import cv2
import pandas as pd

img_path = 'resources/colorpic.jpg'
csv_path = 'resources/colors.csv'

# index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=None, header=0)
img = cv2.imread(img_path)
img = cv2.resize(img, (800, 600))

clicked = False
r = g = b = xpos = ypos = 0


class all_funcs():

    def get_color_name(self, R, G, B):
        minimum = 1000
        for i in range(len(df)):
            d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
            if d <= minimum:
                minimum = d
                cname = df.loc[i, 'color_name']

        return cname

    def draw_function(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            global b, g, r, xpos, ypos, clicked
            clicked = True
            xpos = x
            ypos = y
            b, g, r = img[y, x]
            b = int(b)
            g = int(g)
            r = int(r)

    def execute(self):
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.draw_function)

        while True:
            cv2.imshow('image', img)
            if clicked:
                # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
                cv2.rectangle(img, (20, 20), (800, 60), (b, g, r), -1)

                # Creating text string to display( Color name and RGB values )
                text = self.get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
                # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
                cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2)

                # For very light colours we will display text in black colour
                if r + g + b >= 600:
                    cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2)

            if cv2.waitKey(20) & 0xFF == 27:
                break



cv2.destroyAllWindows()
