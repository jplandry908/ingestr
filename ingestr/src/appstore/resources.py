
from dataclasses import dataclass
from typing import List

@dataclass
class ResourceConfig:
    name: str
    primary_key: List[str]
    columns: dict
    report_name: str

RESOURCES: List[ResourceConfig] = [
    ResourceConfig(
        name="app-downloads-detailed",
        primary_key=[
            "App Apple Identifier",
            "App Name",
            "App Version",
            "Campaign",
            "Date",
            "Device",
            "Download Type",
            "Page Title",
            "Page Type",
            "Platform Version",
            "Pre-Order",
            "Source Info",
            "Source Type",
            "Territory",
        ],
        columns={
            "Date": {"data_type": "date"},
            "App Apple Identifier": {"data_type": "bigint"},
            "Counts": {"data_type": "bigint"},
            "processing_date": {"data_type": "date"},
        },
        report_name="App Downloads Detailed"
    ),
    ResourceConfig(
        name="app-store-discovery-and-engagement-detailed",
        primary_key=[
            "App Apple Identifier",
            "App Name",
            "Campaign",
            "Date",
            "Device",
            "Engagement Type",
            "Event",
            "Page Title",
            "Page Type",
            "Platform Version",
            "Source Info",
            "Source Type",
            "Territory",
        ],
        columns={
            "Date": {"data_type": "date"},
            "App Apple Identifier": {"data_type": "bigint"},
            "Counts": {"data_type": "bigint"},
            "Unique Counts": {"data_type": "bigint"},
            "processing_date": {"data_type": "date"},
        },
        report_name="App Store Discovery and Engagement Detailed"
    ),
    ResourceConfig(
        name="app-sessions-detailed",
        primary_key=[
            "Date",
            "App Name",
            "App Apple Identifier",
            "App Version",
            "Device",
            "Platform Version",
            "Source Type",
            "Source Info",
            "Campaign",
            "Page Type",
            "Page Title",
            "App Download Date",
            "Territory",
        ],
        columns={
            "Date": {"data_type": "date"},
            "App Apple Identifier": {"data_type": "bigint"},
            "Sessions": {"data_type": "bigint"},
            "Total Session Duration": {"data_type": "bigint"},
            "Unique Devices": {"data_type": "bigint"},
            "processing_date": {"data_type": "date"},
        },
        report_name="App Sessions Detailed"
    ),
    ResourceConfig(
        name="app-store-installation-and-deletion-detailed",
        primary_key=[
            "App Apple Identifier",
            "App Download Date",
            "App Name",
            "App Version",
            "Campaign",
            "Counts",
            "Date",
            "Device",
            "Download Type",
            "Event",
            "Page Title",
            "Page Type",
            "Platform Version",
            "Source Info",
            "Source Type",
            "Territory",
            "Unique Devices",
        ],
        columns={
            "Date": {"data_type": "date"},
            "App Apple Identifier": {"data_type": "bigint"},
            "Counts": {"data_type": "bigint"},
            "Unique Devices": {"data_type": "bigint"},
            "App Download Date": {"data_type": "date"},
            "processing_date": {"data_type": "date"},
        },
        report_name="App Store Installation and Deletion Detailed"
    ),
    ResourceConfig(
        name="app-store-purchases-detailed",
        primary_key=[
            "App Apple Identifier",
            "App Download Date",
            "App Name",
            "Campaign",
            "Content Apple Identifier",
            "Content Name",
            "Date",
            "Device",
            "Page Title",
            "Page Type",
            "Payment Method",
            "Platform Version",
            "Pre-Order",
            "Purchase Type",
            "Source Info",
            "Source Type",
            "Territory",
        ],
        columns={
            "Date": {"data_type": "date"},
            "App Apple Identifier": {"data_type": "bigint"},
            "App Download Date": {"data_type": "date"},
            "Content Apple Identifier": {"data_type": "bigint"},
            "Purchases": {"data_type": "bigint"},
            "Proceeds In USD": {"data_type": "double"},
            "Sales In USD": {"data_type": "double"},
            "Paying Users": {"data_type": "bigint"},
            "processing_date": {"data_type": "date"},
        },
        report_name="App Store Purchases Detailed"
    ),
    ResourceConfig(
        name="app-crashes-expanded",
        primary_key=[
            "App Name",
            "App Version",
            "Build",
            "Date",
            "Device",
            "Platform",
            "Release Type",
            "Territory",
        ],
        columns={
            "Date": {"data_type": "date"},
            "processing_date": {"data_type": "date"},
            "App Apple Identifier": {"data_type": "bigint"},
            "Count": {"data_type": "bigint"},
            "Unique Devices": {"data_type": "bigint"},
        },
        report_name="App Crashes Expanded"
    )
]