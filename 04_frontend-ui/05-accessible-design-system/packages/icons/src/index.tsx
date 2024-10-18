/**
 * @aurora-ds/icons — SVG icon library
 *
 * All icons:
 *   - Accept `size` (number, default 16) and all SVG props
 *   - Accept `aria-label` for decorative vs meaningful use
 *   - Rendered at 1em×1em by default for text-size alignment
 *   - Stroke-based, 1.5px weight, rounded caps/joins
 *
 * Usage:
 *   <SearchIcon size={20} aria-hidden />  // decorative, hidden from SR
 *   <AlertIcon aria-label="Error" />       // meaningful, read aloud
 */

import React from 'react';

type IconProps = React.SVGAttributes<SVGElement> & {
  size?: number | string;
};

function Icon({ size = 16, children, ...rest }: IconProps & { children: React.ReactNode }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      {...rest}
    >
      {children}
    </svg>
  );
}

export const SearchIcon    = (p: IconProps) => <Icon {...p}><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></Icon>;
export const CloseIcon     = (p: IconProps) => <Icon {...p}><path d="M18 6L6 18M6 6l12 12"/></Icon>;
export const CheckIcon     = (p: IconProps) => <Icon {...p}><path d="M20 6L9 17l-5-5"/></Icon>;
export const ChevronDownIcon = (p: IconProps) => <Icon {...p}><path d="M6 9l6 6 6-6"/></Icon>;
export const ChevronUpIcon = (p: IconProps) => <Icon {...p}><path d="M18 15l-6-6-6 6"/></Icon>;
export const ChevronLeftIcon = (p: IconProps) => <Icon {...p}><path d="M15 18l-6-6 6-6"/></Icon>;
export const ChevronRightIcon = (p: IconProps) => <Icon {...p}><path d="M9 18l6-6-6-6"/></Icon>;
export const AlertCircleIcon = (p: IconProps) => <Icon {...p}><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></Icon>;
export const CheckCircleIcon = (p: IconProps) => <Icon {...p}><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></Icon>;
export const InfoIcon      = (p: IconProps) => <Icon {...p}><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></Icon>;
export const WarningIcon   = (p: IconProps) => <Icon {...p}><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></Icon>;
export const UserIcon      = (p: IconProps) => <Icon {...p}><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></Icon>;
export const UsersIcon     = (p: IconProps) => <Icon {...p}><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></Icon>;
export const SettingsIcon  = (p: IconProps) => <Icon {...p}><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 010 14.14M4.93 4.93a10 10 0 000 14.14"/></Icon>;
export const TrashIcon     = (p: IconProps) => <Icon {...p}><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/><path d="M10 11v6M14 11v6"/><path d="M9 6V4h6v2"/></Icon>;
export const EditIcon      = (p: IconProps) => <Icon {...p}><path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/></Icon>;
export const PlusIcon      = (p: IconProps) => <Icon {...p}><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></Icon>;
export const MinusIcon     = (p: IconProps) => <Icon {...p}><line x1="5" y1="12" x2="19" y2="12"/></Icon>;
export const ExternalLinkIcon = (p: IconProps) => <Icon {...p}><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></Icon>;
export const CopyIcon      = (p: IconProps) => <Icon {...p}><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></Icon>;
export const DownloadIcon  = (p: IconProps) => <Icon {...p}><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></Icon>;
export const UploadIcon    = (p: IconProps) => <Icon {...p}><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></Icon>;
export const RefreshIcon   = (p: IconProps) => <Icon {...p}><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0114.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0020.49 15"/></Icon>;
export const FilterIcon    = (p: IconProps) => <Icon {...p}><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></Icon>;
export const SortIcon      = (p: IconProps) => <Icon {...p}><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></Icon>;
export const EyeIcon       = (p: IconProps) => <Icon {...p}><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></Icon>;
export const EyeOffIcon    = (p: IconProps) => <Icon {...p}><path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94"/><path d="M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19"/><line x1="1" y1="1" x2="23" y2="23"/></Icon>;
export const MenuIcon      = (p: IconProps) => <Icon {...p}><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></Icon>;
export const MoonIcon      = (p: IconProps) => <Icon {...p}><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></Icon>;
export const SunIcon       = (p: IconProps) => <Icon {...p}><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></Icon>;
export const HomeIcon      = (p: IconProps) => <Icon {...p}><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></Icon>;
export const BellIcon      = (p: IconProps) => <Icon {...p}><path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></Icon>;
export const LockIcon      = (p: IconProps) => <Icon {...p}><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></Icon>;
export const MailIcon      = (p: IconProps) => <Icon {...p}><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></Icon>;
export const CalendarIcon  = (p: IconProps) => <Icon {...p}><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></Icon>;
export const ClockIcon     = (p: IconProps) => <Icon {...p}><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></Icon>;
export const TagIcon       = (p: IconProps) => <Icon {...p}><path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></Icon>;
export const CommandIcon   = (p: IconProps) => <Icon {...p}><path d="M18 3a3 3 0 00-3 3v12a3 3 0 003 3 3 3 0 003-3 3 3 0 00-3-3H6a3 3 0 00-3 3 3 3 0 003 3 3 3 0 003-3V6a3 3 0 00-3-3 3 3 0 00-3 3 3 3 0 003 3h12a3 3 0 003-3 3 3 0 00-3-3z"/></Icon>;
