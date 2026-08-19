#!/usr/bin/env python3
# main.py - Spammer OTP WhatsApp (MONZ XTER)
# ============================================================
# OWNER : MONZ XTER
# ============================================================

import sys
import time
from colorama import Fore, Style

# ===== IMPOR DARI LICENSE & MAIN_ENGINE (TETAP JALAN) =====
from license import (
    clear_screen, log_info, log_success, log_warning, log_error, log_input,
    check_license, use_quota, get_device_id, check_user,
    get_trial_quota
)

# ============================================================
# 🔥 MENU UTAMA – MONZ XTER
# ============================================================
def show_menu():
    print(Fore.CYAN + "=== MONZ XTER OTP SPAMMER ===" + Style.RESET_ALL)
    print(Fore.YELLOW + "[1] Single Round" + Style.RESET_ALL)
    print(Fore.YELLOW + "[2] Infinite Loop" + Style.RESET_ALL)
    print(Fore.YELLOW + "[3] Keluar" + Style.RESET_ALL)
    print(Fore.RED + "-----------------------------" + Style.RESET_ALL)

# ============================================================
# 📱 FUNGSI UTAMA
# ============================================================
def main():
    # Cek lisensi (premium / trial) – tetap jalan seperti asli
    status, quota, device_id = check_license()

    if status == "trial":
        trial_quota = get_trial_quota()
        while True:
            clear_screen()
            show_menu()
            print(f"{Fore.YELLOW}Mode Trial – Sisa Kuota: {quota}/{trial_quota}{Style.RESET_ALL}")
            print()
            choice = log_input("Pilih (1/2/3): ").strip()

            if choice == '1':
                if quota <= 0:
                    log_warning("Kuota trial habis!")
                    log_info("Silakan beli lisensi premium.")
                    input("Tekan Enter...")
                    continue
                from main_engine import run_single_round
                run_single_round(threads=1)
                if use_quota(device_id):
                    user = check_user(device_id)
                    if user:
                        quota = user.get("quota", 0)
                        log_info(f"Sisa kuota: {quota}/{trial_quota}")
                else:
                    log_error("Gagal mengurangi kuota!")
                input("Tekan Enter untuk kembali...")
            elif choice == '2':
                log_info("Mode trial hanya bisa Single Round.")
                input("Tekan Enter...")
            elif choice == '3':
                log_info("Keluar dari MONZ XTER...")
                sys.exit(0)
            else:
                log_warning("Pilihan tidak valid!")
                input("Tekan Enter...")

    elif status == "premium":
        while True:
            clear_screen()
            show_menu()
            print(f"{Fore.GREEN}⚡ Premium Active – Full Access ⚡{Style.RESET_ALL}")
            print(f"{Fore.CYAN}🔥 Selamat datang, !{Style.RESET_ALL}")
            print()
            choice = log_input("Pilih (1/2/3): ").strip()

            if choice == '1':
                from main_engine import run_single_round
                # Pilih thread (opsional)
                thread_choice = input(Fore.YELLOW + "Thread (1-10, enter=1): " + Style.RESET_ALL).strip()
                try:
                    threads = int(thread_choice) if thread_choice else 1
                    threads = max(1, min(threads, 10))
                except:
                    threads = 1
                run_single_round(threads=threads)
                input("Tekan Enter untuk kembali...")
            elif choice == '2':
                from main_engine import run_infinite_loop
                run_infinite_loop()
                input("Tekan Enter untuk kembali...")
            elif choice == '3':
                log_info("Keluar dari MONZ XTER...")
                sys.exit(0)
            else:
                log_warning("Pilihan tidak valid!")
                input("Tekan Enter...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nKeluar dari Sc spammer...." + Style.RESET_ALL)
        sys.exit(0)