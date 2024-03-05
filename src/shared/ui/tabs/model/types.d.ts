export interface ITabs {
  tabs: Tab[];
  activeTab: number;
  marginCorner: 'small' | 'medium'
}

interface Tab {
  label: string;
}
