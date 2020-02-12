def update_ui(self):
    ret, frame = self.cam_capture.read()

    if self.results_pending:
        if not path.isfile('output.jpg'):
            self.results_pending = False
            with open('.out') as content_file:
                content = content_file.readlines()[2:-2]
            system('rm .out')
            self.handle_image_classification(content)

    if self.take_picture:
        cv2.imwrite('output.jpg', frame)
        self.user_prompt.setText('Please wait...')
        system('./classifyimage.py --mean mean.binaryproto --nogpu --labels labels.txt model.caffemodel deploy.prototxt output.jpg > .out && rm output.jpg')
        self.take_picture = False
        self.results_pending = True

    image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
    pix = QPixmap.fromImage(image)
    self.video_frame.setPixmap(pix)

def update_bar_graph(self, data):
    palette = QPalette()
    palette.setColor(QPalette.Background, Qt.white)
    for i in range(0, 8):
        self.bar_graph_labels[i].setText(str(data[i]) + "%")
        height = int(data[i] * 5)
        self.bar_graph[i].setFixedSize(self.bar_width, height)
        self.bar_graph[i].move(1280 + (i * (self.bar_width + self.bar_spacing)), 640 - height)

def handle_image_classification(self, raw_output):
    data = [None] * 8
    for i in range(0, len(raw_output)):
        raw_output[i] = raw_output[i].strip()
        data[int(raw_output[i][-2]) - 1] = float(raw_output[i][:-10])
    self.update_bar_graph(data)