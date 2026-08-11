import os

def main():
    print("==================================================")
    print("  Bluestock Mutual Fund Analytics - Pipeline v1.0 ")
    print("==================================================")
    
    print("\n[1/3] Running Data Cleaning & DB Build...")
    if os.path.exists("db_build.py"):
        os.system("python db_build.py")
    
    print("\n[2/3] Executing EDA & Chart Generation...")
    if os.path.exists("notebooks/eda_script.py"):
        os.system("python notebooks/eda_script.py")
    
    print("\n[3/3] Running Fund Performance Analytics...")
    if os.path.exists("notebooks/performance_analytics.py"):
        os.system("python notebooks/performance_analytics.py")
    
    print("\n==================================================")
    print("  Pipeline Execution Complete Successfully!      ")
    print("==================================================")

if __name__ == "__main__":
    main()
