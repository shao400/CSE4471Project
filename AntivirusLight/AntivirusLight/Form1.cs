using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AntivirusLight
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        
        /* Function used to get MD5 from a file */
        private string GetMD5FromFile(String filePath)
        {
            using (var md5 = MD5.Create())
            {
                using (var stream = File.OpenRead(filePath))
                {
                    /* Return MD5 and present it with every "-" removed and to lower case */
                    return BitConverter.ToString(md5.ComputeHash(stream)).Replace("-",string.Empty).ToLower();
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void bttnScan_Click(object sender, EventArgs e)
        {
            var md5Signatures = File.ReadAllLines("MD5Base.txt");
            if (md5Signatures.Contains(txtMD5.Text))
            {
                lblStatus.Text = "File Infected!";
                lblStatus.ForeColor = Color.Red;
            }
            else 
            {
                lblStatus.Text = "File Clean!";
                lblStatus.ForeColor = Color.Green;
            }
        }
   

        /* Browse button */
        private void bttnBrowse_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            //ofd.Filter = "Textfiles | *.txt";
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                FileInfo f = new FileInfo(ofd.FileName);
                txtFile.Text = f.FullName;
                txtMD5.Text = GetMD5FromFile(ofd.FileName); /* File text box*/
            }
            lblStatus.Text = "N/A";
            lblStatus.ForeColor = Color.Black;
        }

        /* Copy MD5 to Clipboard */
        private void bttnCopy_Click(object sender, EventArgs e)
        {
            Clipboard.SetText(txtMD5.Text);
        }

        private void exitToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

    }
}
