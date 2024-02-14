import type { IconName, Priority } from "@/shared/assets/icons";


export interface IEventCard {
  title: string
  day: string
  time: string
  startTime?: string
  priority?: Priority
}
