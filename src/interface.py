import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for Linux/WSL
import matplotlib.pyplot as plt
import sys
import os
import subprocess

class InteractiveInterface:
    """Interactive menu-based interface for navigating charts"""
    
    def __init__(self, chart_generator, total_charts=10):
        self.chart_generator = chart_generator
        self.total_charts = total_charts
        
        self.chart_methods = [
            ('Sales by Genre (Bar Chart)', self.chart_generator.chart_1_sales_by_genre_bar),
            ('Sales Trend Over Years (Line Chart)', self.chart_generator.chart_2_sales_trend_line),
            ('Market Share by Platform (Pie Chart)', self.chart_generator.chart_3_market_share_pie),
            ('Price vs Rating (Scatter Plot)', self.chart_generator.chart_4_price_vs_rating_scatter),
            ('Rating Distribution (Histogram)', self.chart_generator.chart_5_rating_distribution_histogram),
            ('Correlation Matrix (Heatmap)', self.chart_generator.chart_6_correlation_heatmap),
            ('ROI by Publisher (Box Plot)', self.chart_generator.chart_7_roi_by_publisher_box),
            ('Playtime by Genre (Violin Plot)', self.chart_generator.chart_8_playtime_by_genre_violin),
            ('Revenue Over Years (Area Chart)', self.chart_generator.chart_9_stacked_revenue_area),
            ('Player Count vs Sales (Bubble Chart)', self.chart_generator.chart_10_player_count_power_bubble)
        ]
    
    def display_menu(self):
        """Display main menu"""
        while True:
            plt.close('all')
            print("\n" + "="*80)
            print("VIDEO GAME ANALYTICS DASHBOARD - CHART MENU")
            print("="*80)
            print("\nSelect a chart to view:")
            print("-" * 80)
            
            for i, (name, _) in enumerate(self.chart_methods, 1):
                print(f"  {i}. {name}")
            
            print("-" * 80)
            print(f"  0. EXIT")
            print("="*80)
            
            try:
                choice = input("\nEnter chart number (0-10): ").strip()
                
                if choice == '0':
                    print("\nThank you for using the Analytics Dashboard!")
                    plt.close('all')
                    break
                
                chart_num = int(choice)
                
                if 1 <= chart_num <= self.total_charts:
                    self.display_chart(chart_num - 1)
                else:
                    print("\nERROR: Invalid selection. Please enter a number between 0-10.")
                    try:
                        input("Press Enter to continue...")
                    except EOFError:
                        break
            
            except ValueError:
                print("\nERROR: Please enter a valid number.")
                try:
                    input("Press Enter to continue...")
                except EOFError:
                    break
            except KeyboardInterrupt:
                print("\n\nExiting...")
                plt.close('all')
                break
            except EOFError:
                print("\n\nEnd of input detected. Exiting...")
                plt.close('all')
                break
    
    def display_chart(self, chart_index):
        """Display selected chart and save as PNG"""
        chart_name, chart_method = self.chart_methods[chart_index]
        
        print(f"\nLoading: {chart_name}...")
        
        try:
            # Create output directory if it doesn't exist
            output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate chart
            fig = chart_method()
            
            # Improve figure appearance
            fig.suptitle('ANALYTICS DASHBOARD', fontsize=16, fontweight='bold', y=0.98)
            
            plt.tight_layout()
            
            # Save chart as PNG
            filename = f"chart_{chart_index + 1}.png"
            filepath = os.path.join(output_dir, filename)
            plt.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
            print(f"✓ Chart saved: {filepath}")
            
            # Try to open with default image viewer
            try:
                if os.path.exists('/mnt/c/Windows/System32/cmd.exe'):  # WSL
                    # Convert WSL path to Windows path
                    windows_path = subprocess.check_output(['wslpath', '-w', filepath]).decode().strip()
                    subprocess.Popen(['cmd.exe', '/c', 'start', windows_path], 
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    print(f"✓ Opening chart in Windows default viewer...")
                else:  # Native Linux
                    subprocess.Popen(['xdg-open', filepath], 
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    print(f"✓ Opening chart with default viewer...")
            except Exception:
                print(f"  (View the chart manually at: {filepath})")
            
            plt.close(fig)
            
            input("\nPress Enter to return to menu...")
            
        except Exception as e:
            print(f"ERROR displaying chart: {str(e)}")
            input("Press Enter to return to menu...")
    
    def run(self):
        """Run interactive menu"""
        self.display_menu()
