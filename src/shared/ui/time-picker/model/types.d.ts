export interface IIosSelect {
  value?: string | number;
  count: number
  source: { text: string | number; value: any }[];
  sensitivity: number;
}
