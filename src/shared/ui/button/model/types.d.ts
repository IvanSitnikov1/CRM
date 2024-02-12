export interface IButton {
  title: string
  type: 'submit' | 'button' | 'reset'
  isFull?: boolean;
  iconNameLeft?: string;
  iconNameRight?: string;
}
