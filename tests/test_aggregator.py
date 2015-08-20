import unittest

import monasca_agent.common.aggregator as aggregator
import monasca_agent.common.metrics as metrics_pkg


class TestMetricsAggregator(unittest.TestCase):
    def setUp(self):
        self.aggregator = aggregator.MetricsAggregator("Foo")

    def submit_metric(self, name, value, dimensions=None, value_meta=None):
        try:
            self.aggregator.submit_metric(name,
                                          value,
                                          metrics_pkg.Gauge,
                                          dimensions=dimensions,
                                          delegated_tenant=None,
                                          hostname=None,
                                          device_name=None,
                                          value_meta=value_meta)
        except Exception:
            pass

    def testValidMetric(self):
        dimensions = {'A': 'B', 'B': 'C', 'D': 'E'}
        value_meta = {"This is a test": "test, test, test"}
        self.submit_metric("Foo",
                           5,
                           dimensions=dimensions,
                           value_meta=value_meta)

        self.assertRaises(None)

    def testInValidMetricName(self):
        dimensions = {'A': 'B', 'B': 'C', 'D': 'E'}
        value_meta = {"This is a test": "test, test, test"}
        self.submit_metric("TooLarge" * 255,
                           5,
                           dimensions=dimensions,
                           value_meta=value_meta)

        self.assertRaises(aggregator.InvalidMetricName)
