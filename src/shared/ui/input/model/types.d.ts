import type { IconName } from "@/shared/assets/icons";

export interface IUIInput{
  placeholder?: string
  title?: string;
  iconName?: IconName;
  iconColor?: string;
  name: string;
  type: 'password' | 'text' | 'email' | 'tel';
  value: string;
  isRequired?: boolean;
  isReadonly?: boolean;
}
