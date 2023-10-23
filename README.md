## Анализ и фильтрация злонамеренного сетевого трафика

#### Цель: 
Разработать модель, которая будет классифицировать входящий трафик на нормальный и злонамеренный.

#### Описание:
Компания онлайн-сервис с высоким уровнем входящего трафика имеет специализированный отдел безопасности, который занимается фильтрацией и анализом трафика. Сотрудники этого отдела обратились за помощью в автоматизации выявления аномального и злонамеренного трафика. Моя задача - разработать модель, которая будет классифицировать входящий трафик на нормальный и злонамеренный, включая следующие типы атак: DDoS, SQL-инъекции, брутфорс, вредоносные программы и т.д.

#### Итоги работы:
В этом проекте нужно было построить модель многоклассовой классификации с целью автоматизации выявления аномального и злонамеренного трафика. Было обучено три модели, сравнили метрики качества и выбрали итоговую. Для итоговой модели был проведен анализ важности признаков и поставлен эксперимент по улучшению качества путем удаления ряда признаков с низким рейтингом важности. По итогу обобщения всех экспериментов с моделированием, была выбрана финальная модель.

Для финальной модели получили достаточно хорошие метрики и разработали REST API сервис, который позволяет выполнять предсказания с использованием лучшей модели. В этом сервисе использовали Python, библиотеку Flask и Docker.

**В процессе работы столкнулась с трудностями:**

В данных изначально очень сильный дисбаланс. По этой причине не удалось достичь высокой точности  по 2-ум классам: Web Attack � Brute Force и Web Attack � XSS - в этих классах слишком мало записей. 

Варианты для дальнейшей доработки: 
- попробовать применить увеличение выборки или балансировку для малочисленных классов,
- объединить WEB атаки в один класс и пытаться предсказывать сначала их, а потом обучить доп классификатор (путнем создания дополнительных признаков) чтобы уже внутри WEB атак определять, какая именно.
