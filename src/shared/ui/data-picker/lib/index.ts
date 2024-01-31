import {
  startOfMonth,
  endOfMonth,
  startOfWeek,
  endOfWeek,
  addMonths,
  subMonths,
  format,
  isSameMonth,
  addDays,
  isSunday,
  isSaturday,
} from 'date-fns';

export interface DateInfo {
  day: number;
  isPrevMonth?: boolean;
  isCurrentMonth?: boolean;
  isNextMonth?: boolean;
  isSelected?: boolean;
}

export class Calendar {
  private currentDate: Date;

  constructor() {
    this.currentDate = new Date();
  }

  goToNextMonth(): void {
    this.currentDate = addMonths(this.currentDate, 1);
  }

  goToPreviousMonth(): void {
    this.currentDate = subMonths(this.currentDate, 1);
  }

  getCalendar(): DateInfo[][] {
    const firstDayOfMonth = startOfMonth(this.currentDate);
    const lastDayOfMonth = endOfMonth(this.currentDate);
    const startDate = startOfWeek(firstDayOfMonth, { weekStartsOn: 1 });
    const endDate = endOfWeek(lastDayOfMonth, { weekStartsOn: 1 });

    let currentDate = startDate;
    const calendar: DateInfo[][] = [];

    for (let row = 0; row < 5; row++) {
      const week: DateInfo[] = [];

      for (let col = 0; col < 5; col++) {
        while (isSunday(currentDate) || isSaturday(currentDate)) {
          currentDate = addDays(currentDate, 1);
        }

        const dateInfo: DateInfo = {
          day: currentDate.getDate(),
          isPrevMonth: !isSameMonth(currentDate, this.currentDate) && currentDate < firstDayOfMonth,
          isCurrentMonth: isSameMonth(currentDate, this.currentDate),
          isNextMonth: !isSameMonth(currentDate, this.currentDate) && currentDate > lastDayOfMonth,
          isSelected: false, // You can set this based on your selection logic
        };

        week.push(dateInfo);
        currentDate = addDays(currentDate, 1);
      }

      calendar.push(week);
    }

    return calendar;
  }

  getCurrentMonth(): string {
    return format(this.currentDate, 'MMMM yyyy');
  }
}
