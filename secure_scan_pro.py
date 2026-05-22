import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
import subprocess
import json
import socket
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SecureScanPro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🔒 SECURE SCAN PRO v2.0 -  Professional Cyber Tool")
        self.geometry("1400x800")
        self.running = False
        self.scan_results = []
        
        # Title
        title = ctk.CTkLabel(self, text="SCANIFY SCANNER", 
                           font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=20)
        
        # Input frame
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(input_frame, text="Targets (comma separated):").pack(pady=5)
        self.target_var = ctk.CTkEntry(input_frame, height=35, 
                                     placeholder_text="scanme.nmap.org, google.com, 8.8.8.8, facebook.com")
        self.target_var.pack(pady=5, padx=10, fill="x")
        
        # Scan type
        ctk.CTkLabel(input_frame, text="Scan Mode:").pack(pady=(20,5))
        self.scan_type = ctk.CTkOptionMenu(input_frame, values=["Quick Scan", "Aggressive (-A)", "Top 1000 Ports", "UDP Scan (-sU)"])
        self.scan_type.pack(pady=5)
        self.scan_type.set("Quick Scan")
        
        # Control buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=20)
        
        self.scan_btn = ctk.CTkButton(btn_frame, text="🚀 START SCAN", height=40, 
                                    command=self.start_scan, fg_color="#28a745")
        self.scan_btn.pack(side="left", padx=10)
        
        self.stop_btn = ctk.CTkButton(btn_frame, text="⏹️ STOP SCAN", height=40, 
                                    command=self.stop_scan, fg_color="#dc3545", state="disabled")
        self.stop_btn.pack(side="left", padx=10)
        
        self.export_btn = ctk.CTkButton(btn_frame, text="💾 EXPORT REPORT", height=40, 
                                      command=self.export_report)
        self.export_btn.pack(side="left", padx=10)
        
        # Log area
        self.log_text = ctk.CTkTextbox(self, height=400)
        self.log_text.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Status
        self.status_var = ctk.CTkLabel(self, text="🟢 READY - Enter targets and START SCAN", 
                                     font=ctk.CTkFont(size=14))
        self.status_var.pack(pady=10)
        
        # Shortcuts
        self.bind('<Escape>', lambda e: self.stop_scan())
        self.bind('<Control-s>', lambda e: self.export_report())
    
    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert("end", f"[{timestamp}] {msg}\n")
        self.log_text.see("end")
        self.update()
    
    def update_status(self, msg):
        self.status_var.configure(text=msg)
    
    def start_scan(self):
        targets = self.target_var.get().strip()
        if not targets:
            messagebox.showerror("Error", "ENTER THE TARGETS IDIOT! (comma separated)")
            return
        
        self.running = True
        self.scan_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.update_status("🔄 SCANNING...")
        
        threading.Thread(target=self.scan_thread, args=(targets,), daemon=True).start()
    
    def stop_scan(self):
        self.running = False
        self.scan_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.update_status("🛑 SCAN STOPPED")
        self.log("🛑 Manual STOP by user")
    
    def scan_thread(self, targets_str):
        try:
            targets = [t.strip() for t in targets_str.split(',')]
            self.log(f"🎯 {len(targets)} targets queued: {targets}")
            scan_mode = self.scan_type.get()
            
            for i, target in enumerate(targets, 1):
                if not self.running:
                    self.log("⏹️ Queue stopped by user")
                    break
                
                self.log(f"\n{'='*60}")
                self.log(f"🎯 SCAN {i}/{len(targets)}: {target} [{scan_mode}]")
                self.log(f"{'='*60}")
                
                cmd = ["nmap"]
                
                # # Scan mode logic
                # if "Aggressive" in scan_mode:
                #     cmd.extend(["-A", "-T4", "-n", target])
                if "Aggressive" in scan_mode:
                    cmd.extend(["-A", "-T4", "-Pn", target])  # -Pn = Skip host discovery
                elif "Top 1000" in scan_mode:
                    # cmd.extend(["--top-ports", "1000", "-sV", "-n", target])
                    cmd.extend(["--top-ports", "1000", "-sV", "-Pn", target])
                elif "UDP" in scan_mode:
                    # cmd.extend(["-sU", "--top-ports", "100", "-T4", target])
                    cmd.extend(["-sU", "--top-ports", "100", "-T4", "-Pn", target])
                else:  # Quick
                    # cmd.extend(["-sV", "--top-ports", "100", "-n", target])
                    cmd.extend(["-sV", "--top-ports", "100", "-Pn", target])
                    
                
                # Execute scan
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
                    if result.returncode == 0:
                        self.log(result.stdout)
                        self.scan_results.append({
                            "target": target,
                            "mode": scan_mode,
                            "output": result.stdout,
                            "time": str(datetime.now())
                        })
                    else:
                        self.log(f"❌ Nmap error: {result.stderr}")
                        
                except subprocess.TimeoutExpired:
                    self.log(f"⏰ Timeout (3 min) on {target}")
                except Exception as e:
                    self.log(f"❌ Scan error: {str(e)}")
            
            if self.running:
                self.log("\n🎉 ALL SCANS COMPLETE! 💾 Use EXPORT REPORT")
                self.update_status(f"✅ COMPLETE - {len(self.scan_results)} targets scanned")
        
        except Exception as e:
            self.log(f"❌ Thread error: {str(e)}")
        finally:
            self.running = False
            self.scan_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")
    
    def export_report(self):
        if not self.scan_results:
            messagebox.showwarning("Warning", "FIRST SCAN IT!")
            return
        
        filename = f"secure_scan_pro_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(self.scan_results, f, indent=2, ensure_ascii=False)
        
        self.log(f"💾 Report saved: {filename}")
        messagebox.showinfo("Success", f"Professional report saved!\n{filename}")
        self.update_status(f"📊 Report exported: {filename}")

if __name__ == "__main__":
    app = SecureScanPro()
    app.mainloop()