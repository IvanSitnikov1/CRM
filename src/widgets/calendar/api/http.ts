import { http } from '@/shared/api';

export const getEventForMonth = async () => {
  const tempUser = 'string';
  const { data } = await http.get(`http://localhost:3000/events/month/${tempUser}`);
  const eventCounts: Map<number, number> = new Map();

  data.result.forEach((day) => {
    const startTime = new Date(day.startTime);
    const dayTimestamp = new Date(startTime.getFullYear(), startTime.getMonth(), startTime.getDate()).getTime();

    if (eventCounts.has(dayTimestamp)) {
      eventCounts.set(dayTimestamp, eventCounts.get(dayTimestamp)! + 1);
    } else {
      eventCounts.set(dayTimestamp, 1);
    }
  });

  return eventCounts;
};
