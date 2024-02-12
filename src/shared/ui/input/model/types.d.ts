
export interface IUIInput{
  placeholder?: string
  title?: string;
  iconName?: string;
  iconColor?: string;
  name: string;
  type: 'password' | 'text' | 'email' | 'tel';
  value: string;
}
