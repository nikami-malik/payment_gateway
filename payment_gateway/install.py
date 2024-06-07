# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt


def after_install():
    import subprocess

    from frappe.utils import get_bench_relative_path

    file_path = get_bench_relative_path("env/bin/pip")

    subprocess.check_output([file_path, "install", "xendit-python==5.0.0", "midtransclient==1.4.2"])