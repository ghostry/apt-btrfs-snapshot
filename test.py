#!/usr/bin/python3
from apt_btrfs_snapshot import AptBtrfsSnapshot
if __name__ == '__main__':
    apt_btrfs = AptBtrfsSnapshot()
    if not apt_btrfs.snapshots_supported():
        print(_("The system does not support apt-btrfs-snapshot"))
        sys.exit(1)

    apt_btrfs.print_btrfs_root_snapshots_older_than('1d')
