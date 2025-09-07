import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def draw_chart(full_name, lifepath, soul_number, destiny, your_year):
    # Рисува кръгова (donut) диаграма, която визуализира:
    #- Житейски път (вътрешен кръг)
    #- Число на душата и Число на съдбата (среден кръг)
    #- Лична година (външен кръг)

    plt.style.use('ggplot')
    plt.figure(figsize=(12, 10))

    # Вътрешен кръг - Житейски път
    plt.pie([100], radius=0.5, wedgeprops=dict(width=0.25),
            colors=['#ff9999'], startangle=90)
    plt.text(0, 0.05, f'{lifepath}', ha='center', va='center',
             fontsize=18, fontweight='bold', color='black')
    plt.text(0, -0.1, 'Житейски път', ha='center', va='center',
             fontsize=9, fontweight='bold', color='black')

    # Среден кръг - Душа и Съдба
    plt.pie([50, 50], radius=0.9, wedgeprops=dict(width=0.25),
            colors=['#66b3ff', '#99ff99'], startangle=90)

    middle_radius = 0.9 - 0.25/2
    # Душа (десен полукръг)
    x1 = middle_radius * np.cos(np.radians(0))
    y1 = middle_radius * np.sin(np.radians(0))
    plt.text(x1, y1+0.05, f'{soul_number}', ha='center', va='center',
             fontsize=16, fontweight='bold', color='white')
    plt.text(x1, y1-0.05, 'Душа', ha='center', va='center',
             fontsize=9, fontweight='bold', color='white')

    # Съдба (ляв полукръг)
    x2 = middle_radius * np.cos(np.radians(180))
    y2 = middle_radius * np.sin(np.radians(180))
    plt.text(x2, y2+0.05, f'{destiny}', ha='center', va='center',
             fontsize=16, fontweight='bold', color='white')
    plt.text(x2, y2-0.05, 'Съдба', ha='center', va='center',
             fontsize=9, fontweight='bold', color='white')

    # Външен кръг - Лична година
    plt.pie([100], radius=1.3, wedgeprops=dict(width=0.25),
            colors=['#ffcc99'], startangle=90)
    outer_radius = 1.3 - 0.25/2
    plt.text(0, outer_radius, f'{your_year}', ha='center', va='center',
             fontsize=18, fontweight='bold', color='#8B4513')
    plt.text(0, outer_radius-0.1, 'Лична година', ha='center', va='center',
             fontsize=10, fontweight='bold', color='#8B4513')

    # Заглавие
    plt.title(f'Нумерологична карта на {full_name}', fontsize=18, pad=30, fontweight='bold')
    plt.axis('equal')

    # Легенда
    legend_elements = [
        mpatches.Rectangle((0, 0), 1, 1, facecolor='#ff9999', label=f'Житейски път: {lifepath}'),
        mpatches.Rectangle((0, 0), 1, 1, facecolor='#66b3ff', label=f'Число на душата: {soul_number}'),
        mpatches.Rectangle((0, 0), 1, 1, facecolor='#99ff99', label=f'Число на съдбата: {destiny}'),
        mpatches.Rectangle((0, 0), 1, 1, facecolor='#ffcc99', label=f'Лична година: {your_year}')
    ]
    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.15, 1), fontsize=12)

    plt.tight_layout()
    plt.show()
