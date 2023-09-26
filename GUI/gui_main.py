from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QVBoxLayout, QFileDialog, QTreeWidgetItem, QMessageBox
from GUI.ui.win import Ui_MainWindow
from GUI.page_function.win import Node_Form, Whoami_Form, Sender_Form
from function_blockchain.server import start_server
from multiprocessing import Process
import requests
import json



class MyWindow(QMainWindow):  

    my_thread = None
    RINNING = False

    @classmethod
    def set_RINNING(cls):
        if not cls.RINNING:
            cls.RINNING = True
        else:
            cls.RINNING = False

    def __init__(self) -> None:
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.my_document = []

        #Обьявление основыых элементов
        self.my_profile_btn =  self.ui.pushButton
        self.nodes_btn =  self.ui.pushButton_2
        self.document_btn = self.ui.pushButton_3
        self.mine_btn = self.ui.mine_pushButton
        self.whoami_form = Whoami_Form()
        self.node_form = Node_Form()
        self.sender_form = Sender_Form()
        #основные элементы whoami
        self.whoami_ip_input = self.whoami_form.ui.lineEdit_ip
        self.whoami_port_input = self.whoami_form.ui.lineEdit_port
        self.main_node_input = self.whoami_form.ui.lineEdit_mainnode
        #основные элементы Node_Form
        self.node_treeviev = self.node_form.ui.nodes_treeWidget
        self.activ_docx_treeviev = self.node_form.ui.activ_docx_treeWidget
        self.node_operation_widget = QStackedWidget(self)
        self.node_operation_widget.addWidget(self.sender_form)
        self.node_form.ui.operation_widget.layout().addWidget(self.node_operation_widget)
        self.node_form.ui.operation_widget.hide()
        # основные элементы Sender_Form
        self.sender_form.ui.buttonBox.accepted.connect(self.send_ok_comlite)
        self.sender_form.ui.buttonBox.rejected.connect(self.close_send_form)
        #Насторой меню форм 
        self.central_widget = QStackedWidget(self)
        self.central_widget.addWidget(self.whoami_form)
        self.central_widget.addWidget(self.node_form)
        self.ui.scrollAreaWidgetContents.setLayout(QVBoxLayout())
        self.ui.scrollAreaWidgetContents.layout().addWidget(self.central_widget)
        # Древесные виджет
        self.node_treeviev.itemClicked.connect(self.func_node_treewidget)
        #Кнопки формы MainForm
        self.my_profile_btn.clicked.connect(self.show_selected_whoami_window)
        self.nodes_btn.clicked.connect(self.show_selected_node_window)
        self.mine_btn.clicked.connect(self.activate_mine_block)
        #Кнопки формы whoami 
        self.whoami_form.ui.startserver_btn.clicked.connect(self.start_server)
        self.whoami_form.ui.add_document_btn.clicked.connect(self.add_document)
        self.whoami_form.ui.connect_node_btn.clicked.connect(self.conncet_blockchain)

    def func_node_treewidget(self,item, column):
        if item.text(column) == "Запросить":
            self.node_form.ui.operation_widget.hide()
        if item.text(column) == "Отправить":
            if self.ip_port != item.parent().text(column)  or True: # тестовая
                if self.my_document:
                    self.node_form.ui.operation_widget.show()         
                    self.sender_form.ui.owner_label.setText(self.ip_port)
                    self.sender_form.ui.recipient_label.setText(item.parent().text(column))
                    self.sender_form.ui.comboBox.clear()
                    self.sender_form.ui.comboBox.addItems(self.my_document)
                    self.node_operation_widget.setCurrentIndex(0)
                else:
                    QMessageBox.information(self,"Ошибка отправки","Нет документов на отпавку")
    def send_ok_comlite(self):
        if self.RINNING:
            d={
                "filename":self.sender_form.ui.comboBox.currentText(),
                "recipient": self.sender_form.ui.recipient_label.text()
            }
            requests.post(f'http://{self.ip_port}/document/sender',json=d)

    def close_send_form(self):
        if self.RINNING:
            self.node_form.ui.operation_widget.hide()        

    def conncet_blockchain(self):
        if self.RINNING:
            d = {"main_node": self.main_node_input.text()}
            response = requests.post(f'http://{self.ip_port}/connect',json=d)
            if response.status_code != 200:
                QMessageBox.information(self,"Ошибка подключения","Не удалос подключиться по адресу "+self.main_node_input.text())
  
    def activate_mine_block(self):
        """ Функционал кнопки, активирующий добычу блока """
        if self.RINNING:
            requests.get(f'http://{str(self.ip_port)}/mine')
            self.update_data() # обновление инфы  

    def show_selected_node_window(self):
        self.node_form.ui.operation_widget.hide()
        self.update_data()  # обновление инфы
        self.central_widget.setCurrentIndex(1)
          

    def update_data(self):
        if self.RINNING:
            response = requests.get(f'http://{str(self.ip_port)}/document/activ')
            if response.status_code == 200:
                response_json = json.loads(response.content.decode())
                document_activ = response_json.get("document")
                if response_json:
                    self.activ_docx_treeviev.clear()
                    self.node_treeviev.clear()
                    self.my_document.clear() 
                    self.whoami_form.ui.mydocx_treeWidget.clear()
                    self.whoami_form.ui.mydocx_treeWidget.setHeaderLabels(['Document','Hash'])
                    self.node_treeviev.setHeaderLabels(['Nodes']) 
                    self.activ_docx_treeviev.setHeaderLabels(['Owner'])
                    if document_activ:  
                        if document_activ.get(self.ip_port):         
                            for doc,hash in document_activ.get(self.ip_port).items():
                                root_docx = QTreeWidgetItem()
                                self.my_document.append(doc)
                                root_docx.setText(0,doc)
                                root_docx.setText(1,hash)
                                self.whoami_form.ui.mydocx_treeWidget.addTopLevelItem(root_docx)
                        for node,docx in document_activ.items():
                            root_docxs = QTreeWidgetItem()
                            root_docxs.setText(0,node)
                            for doc, hash in docx.items():
                                child1 = QTreeWidgetItem(root_docxs)
                                child1.setText(0,doc)   
                                child2 = QTreeWidgetItem(child1)
                                child2.setText(0,'hash: ' + hash)
                            self.activ_docx_treeviev.addTopLevelItem(root_docxs)

                    for node in response_json.get('nodes'):
                        root_nodes = QTreeWidgetItem()
                        root_nodes.setText(0,node)
                        child1 = QTreeWidgetItem(root_nodes)
                        child1.setText(0,"Отправить")
                        child1 = QTreeWidgetItem(root_nodes)
                        child1.setText(0,"Запросить")                  
                        self.node_treeviev.addTopLevelItem(root_nodes)

    def show_selected_whoami_window(self):
        """ Отображение формы Whoami """
        self.update_data()  # обновление инфы
        self.central_widget.setCurrentIndex(0)
        # блок по выводу документов в whoami form 
                                
            
    def start_server(self):
        if not self.RINNING:
            ip = self.whoami_ip_input.text()
            port = self.whoami_port_input.text()
            self.ip_port = ip +":"+port
            self.whoami_port_input.setReadOnly(True)
            self.whoami_port_input.setReadOnly(True)
            # запуск мультипроцесса сервера flask
            self.my_thread = Process(target=start_server, args=(ip, port))
            self.my_thread.start()
            self.set_RINNING()
            self.ui.label_status_server.setText("Сервер: подключен") 
        else:
            self.my_thread.terminate()
            self.set_RINNING()
            self.whoami_port_input.setReadOnly(False)
            self.whoami_port_input.setReadOnly(False)
            self.ui.label_status_server.setText("Сервер: не подключен") 

    def add_document(self):
        if self.RINNING:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly  # Для выбора только существующего файла
            file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "Текстовые файлы (*.docx *.pdf)", options=options)

            if file_path:
                filename = file_path.split('/')[-1]
                d = { "document": filename}
                requests.post(f'http://{str(self.ip_port)}/document/add',json=d)
                
            




    # >pyuic5.exe ui\WhoamiWindow.ui -o ui\whoami_win.py
    