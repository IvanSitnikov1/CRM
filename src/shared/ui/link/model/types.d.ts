import type { IconName } from "@/shared/assets/icons";

export interface ILink {
  title?: string
  to?: string
  iconLeft?: IconName
  iconRight?: IconName
  iconLeftColor?: string
  iconRightColor?: string
}
