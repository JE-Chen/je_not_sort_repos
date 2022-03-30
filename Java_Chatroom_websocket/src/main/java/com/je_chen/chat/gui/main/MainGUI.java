package com.je_chen.chat.gui.main;

import com.je_chen.chat.gui.GuiFather;
import com.je_chen.chat.gui.client.ClientChatGUI;
import com.je_chen.chat.gui.server.ServerChatGui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class MainGUI extends GuiFather {
    private JPanel jPanel;
    private JButton connectButton;
    private JButton serverButton;
    private JTextField connectServerUrl;
    private JLabel connectServerUrlText;
    private JLabel openServerPort;
    private JTextField OpenServerPort;
    private JTextField connectServerPort;
    private JTextField OpenServerUrl;
    private JLabel openServerUrlText;
    private JLabel connectServerPortText;

    public MainGUI(String windowName) {
        super(windowName);
        setContentPane(jPanel);
        setVisible(true);

        connectButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    new Thread(new ClientChatGUI("連線的聊天室", Integer.parseInt(connectServerPort.getText()), connectServerUrl.getText())).start();
                } catch (NumberFormatException exception) {
                    exception.printStackTrace();
                    JOptionPane.showMessageDialog(null, "請輸入正確資訊", "InfoBox: ", JOptionPane.INFORMATION_MESSAGE);
                }
            }
        });

        serverButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String ip = "127.0.0.1";
                if (OpenServerUrl.getText() != null && !OpenServerUrl.getText().equals("")) {
                    ip = OpenServerUrl.getText();
                } else {
                    try (final DatagramSocket socket = new DatagramSocket()) {
                        socket.connect(InetAddress.getByName("8.8.8.8"), 5050);
                        ip = socket.getLocalAddress().getHostAddress();
                    } catch (SocketException | UnknownHostException socketException) {
                        socketException.printStackTrace();
                    }
                }
                try {
                    new Thread(new ServerChatGui("開啟的聊天室" + "IP : " + ip, Integer.parseInt(OpenServerPort.getText()))).start();
                } catch (NumberFormatException exception) {
                    exception.printStackTrace();
                    JOptionPane.showMessageDialog(null, "請輸入正確資訊", "InfoBox: ", JOptionPane.INFORMATION_MESSAGE);
                }
            }
        });
    }

    @Override
    protected void closeEvent() {
        this.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                super.windowClosing(e);
                System.out.println(windowName + " Frame Closed");
                System.exit(0);
            }
        });
    }

}
