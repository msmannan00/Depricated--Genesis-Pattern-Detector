/*
Created by hyperdefined
Help from: https://kodejava.org/generating-md5-digest-from-file-or-inputstream-object/
*/

package space.hyperdefined.hashgenerator;

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import javax.swing.Action;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextPane;

import org.apache.commons.codec.digest.DigestUtils;

public class HashGenerator {

	public static String md5Final = "";
	public static String sha1Final = "";
	public static String sha256Final = "";
	
	public static void main(String[] args) {
				
		//Creates the JFrame and configures it.
		JFrame window = new JFrame("Hash Generator 1.0");
		window.setSize(670, 110);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setLayout(new FlowLayout(FlowLayout.LEFT));
		window.setResizable(false);
		
		//Creates the JPanels.
		JPanel panel = new JPanel();
		window.add(panel);
	
		//Creates the "Choose a file button."
		JButton chooseFile = new JButton("Choose a file");
		panel.add(chooseFile);
		
		//Creates the file chooser with custom options.
		String userDir = System.getProperty("user.home");
		JFileChooser input = new JFileChooser(userDir +"/");
		Action details = input.getActionMap().get("viewTypeDetails");
		details.actionPerformed(null);
		
		// Creates the output text field.
		JTextPane finalText = new JTextPane();
		finalText.setBorder(BorderFactory.createEmptyBorder());
		finalText.setOpaque(false);
		finalText.setEditable(false);
		finalText.setPreferredSize( new Dimension( 520, 60 ) );
		finalText.setText("MD5: \nSHA1: \nSHA-256: ");
		panel.add(finalText);
		
		//This will make the window appear.
		window.setVisible(true);
		
		//Adds a listener for when the button is clicked, it opens the file chooser.
		chooseFile.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent onClick) {
				
				//Opens the file chooser.
				int result = input.showOpenDialog(chooseFile);
				
				//When the file chooser opens, this will save the file and get the checksum.
				if (result == JFileChooser.FILES_ONLY) {
					
						try 
						{
							//Gets the file from the file chooser.
							File finalFile = new File(input.getSelectedFile().getAbsolutePath());
							InputStream is = new FileInputStream(finalFile);
							InputStream is2 = new FileInputStream(finalFile);
							InputStream is3 = new FileInputStream(finalFile);
	
							//Generate the checksum with the given file.
							md5Final = DigestUtils.md5Hex(is);
							sha1Final = DigestUtils.shaHex(is2);
							sha256Final = DigestUtils.sha256Hex(is3);
							
							//Puts the final output into the text box.
							finalText.setText("MD5: " + md5Final + "\nSHA1: " + sha1Final + "\nSHA-256: " + sha256Final);
	
						}
						catch(IOException e) 
						{
							e.printStackTrace();
						}
					}
			}
		});
	}
}