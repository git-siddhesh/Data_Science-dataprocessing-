{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Datavisualization1",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/git-siddhesh/Data_Science-dataprocessing-/blob/Data_processing/Datavisualization1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4expqGMRHyIE",
        "colab_type": "text"
      },
      "source": [
        "#DataVisualisation1"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8gWyKhEkHd83",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "data=pd.read_csv('student.csv')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BOJZ1azHHjex",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 403
        },
        "outputId": "7078c6f3-8c6b-4612-91ec-947bd9330e25"
      },
      "source": [
        "marks=data.iloc[0:,1]\n",
        "names=data.iloc[0:,0]\n",
        "plt.pie(marks,labels=names)\n"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "([<matplotlib.patches.Wedge at 0x7f9c734eac50>,\n",
              "  <matplotlib.patches.Wedge at 0x7f9c7347c0f0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f9c7347c5c0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f9c7347ca90>],\n",
              " [Text(0.785511765394761, 0.7700462755097296, 'siddhesh'),\n",
              "  Text(-0.6710826482161821, 0.8715779249517257, 'rishabh'),\n",
              "  Text(-0.9869627432273725, -0.48570005505568936, 'saloni'),\n",
              "  Text(0.599714261400543, -0.9221403389250474, 'chirag')])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAPMAAADuCAYAAADsvjF6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4zLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvnQurowAAHG5JREFUeJzt3Xl8W+Wd7/HPz7HjbKAkhKEBQhQC\nSQQxhYRlgFCWljZgljJDS++lrULLQDssw51yqe4UqDoDJdxCWxhaSlkuoXTaDi0UGBG2AQqlEJKw\n5CSRHJYYAgmQQAnYjlf97h9HBmMcb5L8nHP0e79efjnY0tHX2F89R0fPeY6oKsaY8KtyHcAYUxpW\nZmMiwspsTERYmY2JCCuzMRFhZTYmIqzMxkSEldmYiLAyGxMRVmZjIsLKbExEWJmNiQgrszERYWU2\nJiKszMZEhJXZmIiwMhsTEVZmYyLCymxMRFiZjYkIK7MxEWFlNiYirMzGRISV2ZiIsDIbExFWZmMi\nwspsTERYmY2JCCuzMRFhZTYmIqpdBzAlko5VARMLH5MKHxOBGP6TtgL5Re0XNT+W31+BFmAb0AS8\nAWxsXFyfdxHdlIaVOUzSsRgwG5jV6/N0/NLKQJuopvMF4NN9fKsznsq8AbwKvNbj41XAa1xc/0Yp\nfgRTPlbmoErHaoFDgCOABcABwC7FbraN0dt7aVWN/6Qwva9vFor+dOFjGbCicXH9tmLzmNIRVXWd\nwQCkYxPwi9v9cRBQW+qHOa3t4rXLdJ99SrCpTmAVfrkfAe5vXFzfXILtmmGyMruUju0InAR8Cfg8\nMKbcD3lK2w8antO9Z5dh09uAB4A7gXsbF9e/V4bHMP2wMo+0dGwicDJ+gY8FRo/kw9e3Xf7SGp2x\nV5kfpgN/tL4T+GPj4vq3y/x4BivzyEnHjgLOxR+Ja1zF+HzblevX6bQZI/iQefwR+1rggcbF9fYH\nVyZW5nJKx8YBX8Mv8VzHaQA4qu3qDY06dZqjh28A/h1Y0ri4vslRhshyPmlERO4TkYn9fL9RRKYM\nYXuLROS6Pr4eF5HVw805JOnYnqRjV+O/f/sLAlJkgA6tdvkOxmzgOuD1eCrzk3gqs6fDLJHj9K0p\nERHgBFWNxmSFdGwG8APgdALwRNmXDpyWuVsMuAA4P57K/Bfw/cbF9c87zhR6I/4HVxghG0TkNmA1\n0CUiU0RkvIhkROQFEVktIqf1uNt5IvKsiHgiMqewnYNF5CkReU5E/iIiPY/QThORx0TkRRH5fo+v\njxKRG0VkjYg8KCJjS/JDpWO7kI5dB+Twd6sDWWSA9mCUuVsV/jGElfFUZkk8lXG1+x8Jrv7o9gZ+\nrqr74s8wAlgIbFTVT6vqXOD+HrffoqrzgOuBCwtfywFHqOoBwKXAD3vc/mDg74H9gC+JyIE9Hvdn\nhcd9r3Cb4UvHYqRjlwMvA+cwwkemhyMgI3NvVcDXgXXxVOaKeCqzo+tAYeSqzK+q6tO9vuYBx4rI\nlSJyhKpu7fG9OwufVwLxwr9jwB2F18E/AfbtcfuHVPUdVd1WuO+CwtfXq+rzfWxraNKxKtKxfwJe\nAf4FGD+s7TjQyShnR9IHYQyQAl6KpzLnxlOZIGcNHFdl/sRMIVVdB8zDL/VlInJpj2+3FT538dHr\n/H8DHi2M4ify8QkXvQ/Rd/93W4+v9dzW4KVjdcBTwE+ByUO+v2MdVAd+7wHYGf+o95p4KvMF12HC\nIjC7XCKyK/Cuqt4uIu8BZw5wlxj+0WKARb2+d6yITMaflfRF4BtFB/TnSl8CXITD94mLoUo+T1Vg\nX8/3YW/g/ngqcwPwHZsu2r8g/WLrgGdE5Hng+8BlA9z+/wJXiMhzfPJJ6RngD/hzh/+gqiuKSpaO\nHQG8AHyPkBa5oMN1gGE6G1gVT2UWDHjLCmaTRvqTjo0BfoR/cGvA0wuDTpWmGW3/McF1jiLkgauB\nSxoX17cNdOPhEJGbgB+r6tpeX18EHKiq5/ZxnyZVnSAiRwEXquoJRWZIA02qetVQ7hekkTlY0rFZ\n+GcEnUsEigyg/plOYVYF/G9gRTyVOaAcD6CqZ/YuclhYmfuSjn0F/2h3Xyfxh5iEdTe7t7nAsngq\nc14xG+lrbkNhfsKBhe+fISLrROQZ4PAe95tRmOPgiUjvl4MTROT3IpITkV8XJkYhIvNF5E8islJE\nHhCRqYWvny8ia0VklYj8tsd29ilkeUVEzh/MzxOYA2CBkI5V4+9WX+A6SjkoEvaRuaca4Np4KrMP\ncF7j4vrh/GzdcxvqAUQkBny78O+p+LP55gNbgUeB5wr3uwa4XlVvE5Fzem3zAPy3STcCTwKHi8gy\n/KPzJ6vq5sKEqMvxD8ymgBmq2tZrWvMc4GhgB6BBRK5X1X6fjG1k7paO7Qw8RESLDJBHulxnKINv\n4R/xnjSM+/Y3t+EQ4DFV3ayq7cDvenzvcOA3hX//qtc2n1HV1wtTlJ/Hn8swG39v4qHCAd6Lgd0L\nt18F/FpEvsrHXwZlVLVNVbcAbzOIVWaszADp2Ez818dHOU5SVhEbmXv6LPB0PJXZeyh3GmBuw4B3\n387X+5rLIMAaVd2/8FGnqp8v3KYe+Fkhx3IRqe5nO/2yMqdj++PvDkX+DJ6IjszdZuG/jj5msHco\nzG1oUdXb8V9ezevx7WXAkSKyk4jU4C8m0e1J4CuFf58+iIdqAHYWkUMLj1sjIvuKSBUwTVUfBb6L\nP3di2O82VHaZ07EjgT9RgoXywiAf3ZG52yTggXgqM9CEo27bndugqpuANP5svyeBbI/7/RNwjoh4\nwG4DPUhhN/1U4EoReQF/9/swYBRwe2E7zwHXquqwl1uq3PeZ07FT8F/3lHzRvKBq0jFr57bdUorF\n/MLggsbF9de4DjGSKnNkTsfOBO6ggooMkKcqGueND85P46nMP7sOMZIqr8zp2BnAjfi7OBWli6qo\n72b3dnU8lblw4JtFQ2WVOR37In6RK1JXZY3M3X4UT2V6vxccSZVTZn91zN9SgSNyt05GVWKZAf49\nnsokXYcot8ooczo2H7iHCnuN3FuFjszgv897czyVKW5lmYCLfpn9EyaW4k+Lq2idWrEjM/h7ZL+K\npzLzBrxlSEW7zOnYFOBB/JUrKl4F72Z3GwvcFU9lIvn3EN0y+9cr/g3buaphJepkVIVOKviYPYA7\n4qlM5E4yim6Z/TXCPuc6RJB0UF3pI3O3I/EXgYyUaJY5HTsJ+D+uYwRNh43MPZ0bT2XOcB2ilKJX\nZv8MqCVEZHWQUuqg2sr8cdfHU5mDXYcolWiVOR0bi7+Q33avXVXJOjRyLxOLVQvcOcxzoQMnWmX2\nT2OL2FI/pdNuI3NfdiMir5+jU+Z0bAHwj65jBFk71fbSo2/JeCqz0HWIYkWjzP6SuDdjr5P71U6N\njczb98t4KhPqiUXRKLN/Yvks1yGCrj3U6/eX3TT8CyuEVvjLnI7N46MrQ5p+tKvtZg/g7Hgqc5Tr\nEMMV7jL7S+PejC0ZPCg2Mg9IgJviqcw410GGI9xlhvOB/V2HCIs2OwA2GDPxX7aFTnjLnI7F8C/k\nZgapnRor8+CcH09ldh/4ZsES3jL7VwII3fWRXWpXK/MgjQGGsoZ2IISzzOnYrvjLnZohaLOReSjO\nGOqi+q6Fs8z+esZjXYcIm3aqw/r7dqEa+FfXIYYifL/cdGw2/gW3zBDZyDxkp8VTmdBMDw5fmf2r\nDlTsonzFaKcmjL9vlwT/ao2hEK5frn9649+5jhFWbVpjT4JDVx9PZQ4f+GbuhavMcB7hyxwYbTYy\nD9d3XAcYjPD8ctOxHYBIrQwx0tqxkXmYToynMru6DjGQ8JQZFgE7ug4RZu1UW5mHpxr4B9chBhKO\nMqdjgr+LbYrQrrabXYQz46lMoJ8Mw/LLPQ4I1Rv4QdROtZ2QMny7Aye6DtGfsJS5Ii78VW72mrlo\n33YdoD/BL3M6Nhn4vOsYUWCvmYt2bDyVmek6xPYEv8z++8q2e1gCHbabXSwhwAfCwlDmL7sOEBUd\namUugVNcB9ieYJc5HdsJONp1jKhoZ5SVuXiz4qlMINebC3aZbRe7pGw3u2QCeVQ76GW2XewS6qR6\ntOsMEXGC6wB9CW6Z07FJ2C52SbVTbSv6lcaCeCoTuEsgBbfMfpHtrZQS6rLXzKVSjT+RKVCCXOZj\nXAeIElU6XGeImMC9brYyVw4rc2kdF09lAtWfQO521S2pm1IdnzZuZnvHnz/X0sLCppbp8c7Oaa5z\nhZyVubQmArOBrOsg3QJZZuCwTpHpDbWjpzfUjuZnkyZSpbppekfn+qNbWjqPa27ZfU57x56uQ4aJ\nIp2uM0TQPKzMA/rEMi15kanrR9dMXT86xi0TY4jqlt06O186oqW1vb65eZe6tva9q4L9ssEpBStz\n6c0Hfu06RLeglvnQgW6gIlNer6mZ8ptYDb+J7QCqW3fp6lp3+LbW5uObmnee39o2uzq4P9+Is5G5\nLOa5DtCTqAbvkr11S+reBSYVtRHV5p3y+YZDtrW+f3xT8+RDt7XOHg21pUkYPh066tW923413XWO\niHkfmNi4uD4QJQrcyFW3pO5vKLbIACLj3xk1at59E8Zz34TxoNoWy+dXzW9te/f45pYdj2jZNnuc\n6vjiE4dDHulynSGCdgT2Al50HQQCWGb8I4SlJ1K7ddSo/R4ZP45Hxo8D1c7xqmv2b23bsrC5ZdzR\nLS2zYnmNleWxAyBPlZW5POZjZd6u8pS5N5HqZpF9nxw3lifHjQWdnB+j2jC3rf2tLzS3jD62uWWv\nnfL5KSOSZQTYyFw284Dfug4BlVzm3kSqWkVmrxg7ZvaKsWO4fMpkRuf15dnt7RuPbWkZtbCpZcbU\nrq6pTrKVQBdVdgCsPAKz8oiVuR/tVTLTG1M70xtTy48nT6Ja9bWZ7R2vfbalheOaWvaId3bu4Trj\nYNludtkE5gneyjwEnSJ7NNSO3qOhdjQ//9hElm1dxzU37zqnvSMwz9K9dVGVd50hogKzOH4Qyxx3\nHWCwPprIUsMtE3f82ESW45ubd9kvQBNZuhhlI3N5fMp1gG6Bep+5bkndeKDJdY6SKUxkOWxba0t9\nU/MUlxNZNurkZw5ru+5gF49dAXZqXFz/rusQQRuZA3fCd1FEYm9VVx901w4TuGuHCd0TWVYdvK31\ng/qm5omHbmudM1ITWTp1lO1ml89UwMrcS7TK3FthIsvSCeNZ2mMiy7zWtr8e39wy4TMt2+aUayJL\nJ6OCswsWPVOBNa5DBK3Mxc/8CpPCRJZHx4/j0Y9PZNm8sLllfCknsnRiI3MZBeKIdtDKHO2ReSB9\nT2RZN7etfdMXmltqi5nIYiNzWe3sOgBYmYPNn8gya8XYMbM+nMii+srstvbXj21pqR7KRJYOqq3M\n5ROIhRKtzCHTLrKnN6Z2zx4TWTbMbO949bMtLSxsbtljRkffE1mszGVlZe6DuA4QNp0i0xpqR0/r\nayLLwubmXROFiSwdGrRfdaQE4n9uIEL00O46QNhtbyLLSStky1kb7n7cdb4o2jp6/PtQ7zpG4Mps\ni86VmIpMeaO6evKCx/+6oTr/hC1OUB6PwE9cZwjGVMMebGQug2Oe1xXVeazI5ROIQcjKXAH+52P5\nil0uaYRYmftgZS6xORs0u0Mrn3adI+IC8XdrZY64f7i/y/mc4QpgI3Mfml0HiJKdtuqm3bdgZ0qV\nXyCeMINW5jdcB4iSMx/IN0hAJjRE3HrXASB4ZX7ddYCoqG3X5nkv6/6uc1SIRtcBIGBl9pJeK/CO\n6xxR8OUn8ivFpseOhG2JXPYt1yEgYGUusNG5WKq6cIWGZrHBkHvVdYBuVuYIOnqVLq/Jh2cttZBr\ndB2gm5U5gk5/ND/adYYK0ug6QLcglnmD6wBhNut1ze24DTvwNXIaXQfoFsQyO19LKczOWtplBxBH\nVqPrAN2CWOaVrgOE1U7v65vTbJLISGt0HaBb4MrsJb0NwGbXOcLomzZJxIVXXAfoFrgyF9joPESj\nO7Rl/ku6n+scFeblRC4bmIHHyhwRX/IniVTWUsXuPeY6QE9BLfOzrgOEiqoev0J3dx2jAj3qOkBP\nQS2zjcxDcKSnK2q6mOE6RwWyMg/ES3qvYmdQDdrXHsnbQa+Rty6Ry250HaKnQJa5YKnrAGGw1xva\nYJNEnAjUqAzBLvN9rgOEwdlLu7a4zlChrMxD8BC2jFC/Jn2gb++xmYNc56hQj7kO0Ftgy+wlvSbg\nCdc5guybD+SzAnZSxchbG5RzmHsKbJkLbFd7O0Z36LYDX9Q61zkqVOB2sSH4Zc64DhBUp/45v6IK\nJrvOUaHudR2gL4Eus5f0GoB1rnMEjqrWL9fdXMeoUK/hH88JnECXueBW1wGC5jOrdUVNF3u6zlGh\n/l8il827DtGXsJS5y3WIIPnaI/mgXfCvUuSBW1yH2J7Al9lLepuwA2EfmrlR18VaOMB1jgr1UCKX\nfc11iO0JfJkLbnYdICjOXtr1tusMFewm1wH6E5YyZ4A3XYdwbdIH+vb0t20lEUc2A3e7DtGfUJTZ\nS3qdwBLXOVz7xoP5tTZJxJnbErlsIC4Qtz2hKHPBTfgHICpSTae2HrTOJok4FOhdbAhRmb2k9xJw\nl+scrvz9k/nlVbCT6xwV6slELptzHWIgoSlzwRWuAzihqics011dx6hg17oOMBihKrOX9FYS0Nk3\n5bRgra4c3cVM1zkq1CrgDtchBqOkZRaRW0Xk1GHe9yQRSQ3ipv86nO2H2df/Ox+qJ92IuTSRy6rr\nEIMRmD8SVb1HVRcPdDsv6f0ZeHAEIgXCnpv0xYnNzHOdo0ItT+SygX47qqcByywi40UkIyIviMhq\nETlNRC4VkeWF//6liEgf9/usiDwnIp6I3CIitYWvN4rID0Tk2cL35hS+vkhErhtk7kuH9FOG2FlL\nuyr+/XWHLnEdYCgGMzIvBDaq6qdVdS5wP3Cdqh5U+O+xwAk97yAiY/DnVJ+mqnVANfDtHjfZoqrz\ngOuBC4ca2kt6y4A/DvV+YRNr0s0z3rJJIo78dyKXfcB1iKEYTJk94FgRuVJEjlDVrcDRIrJMRDzg\nGGDfXveZDaxX1e7TF5cAn+nx/TsLn1fCsK8j/L+AbcO8byh846H8GoFa1zkqUBf+31eoDFjmQiHn\n4Zf6MhG5FPg5cGph1L0RGDPEx20rfO7CH7WHzEt6jcDlw7lvGNR0aushDdr7SdKMjJsTuaznOsRQ\nDeY1865Ai6reDvwIPjwYs0VEJgB9Hb1uAOIislfhv78G/KkEeXv7ERFdvOCUv+SXVyk7u85Rgd4H\nLnYdYjgGs5tdBzwjIs8D3wcuwx+NVwMPAMt730FVW4EzgDsKu+J54BelCt3NS3rtwDml3m4QnLRM\np7rOUKH+LUgXgxsKUQ3FW2j9qltS9zvgy65zlMpha/MrL7g7P991jgr0Z+CoRC4bysUwAvM+c5H+\nGfjAdYhSST6cD/8zbPhsBb4a1iJDRMrsJb03gPNc5yiFGW/qS5OaOdB1jgr0rUQu+6rrEMWIRJkB\nvKS3BLjddY5inbW0a5PrDBXotkQu+1vXIYoVmTIXfBt4yXWI4Yo165Y937TLzYywl4FzXYcohUiV\nuXBJm68Q0mtUnfFgfo0M/T17M3ydwOmJXDYSx1siVWb48DTJwZx9FSjVndr2tw26j+scFSadyGWX\nuQ5RKpErc8FPCdmlbU55yiaJjLDHidhiF5Ess5f0FPgqsNZ1lsE66WndxXWGCvI2/ttQkVpTLpJl\nBvCS3nvA8YRgid5Ds/lnazvZ23WOCvE+sDCRy25wHaTUIltmAC/pvYp/emaz6yz9ST6cj9QIEWCt\nwImJXPY510HKIdJlhg8PiJ1GQK9XNf0tfXlSEzZ1s/w6gdMSuezjroOUS+TLDOAlvQwBPSHj7KVd\nGwU+sVKLKSkFvpnIZe9xHaScKqLMAF7SuwH4oescPe3YrO/M3GSTREbAdxK57G2uQ5RbxZQZwEt6\n38M/hTMQFj2cX22TRMruh4lc9ieuQ4yEiiozgJf0LgH+xXWO6i5tPyyrCdc5Iu4XiVz2e65DjJSK\nKzOAl/SuAC7Afy3lxMlP6fIq5W9cPX4FWEJAj5OUS0WWGcBLetcAZ+PoYnRffCpvs73KQ4GLE7ns\noqhNChlIxZYZwEt6NwJJ/LctRswhufxztZ3MGsnHrBDbgC8nctnILvTYn4ouM4CX9G4HvgC8M1KP\nuejh/Ig+eVSIN4EjE7ns710HcaXiywzgJb1HgAOBF8r9WHu8ra9M/sBWEimxF4CDE7nsJxaXrCRW\n5oLCOtyHAb8r5+OcvbTrDZskUlL3AguiONd6qCKxOmep1S2p+y7+BJOSPtnt0KLv3nRN11jxL+lj\ninc1cFGlHejaHhuZ++AlvSvxT9Ao6frJyYfznhW5JJqAMxK57IVW5I9YmbfDS3pL8a+h9YdSbK+6\nS9sXrNU5pdhWhXsc2C+Ry97qOkjQWJn74SW9zV7SOxX4H8C7xWzrxKf1mSrFFiAYvlb89dGPSuSy\n612HCSJ7zTxIdUvqPgXcAJw0nPvfdlVnw5gOZpc2VcX4C/5ZTznXQYLMRuZB8pLem17SOxn4OkMc\npQ9qyD9nRR6WvwJn4R+ttiIPwMo8RF7S+xWwF/BjBrmk7xkP2SSRYbgdmJPIZW9M5LK2+zgItptd\nhLoldTPwV3g8bXu32X2zrr/6pq64vbc8aE8ClyRy2UddBwkbG5mL4CW99V7S+wpwCPBEX7c5e2nX\nBivyoDwCHJ3IZRcUU2QRuVVEPnHNcBHZVUQiPdXTRuYSqltS90XgEgoXpJ/Qon+9+ZquWoFxbpMF\n2n3AZYlc9qlSbExEbgX+S1UHVVwRqVbVSLwMsjKXQd2Sus8BF51zb1fNkav1KNd5AkiBP+KX+Nli\nNiQiXwcuLGxzFf7Cje/jz7X/FHCRqv5eROL4JZ8rIouAvwMmAKOAeuBuYBJQA1ysqncXtn8J/hrs\nm4ENwEpVvaqYzOViZS6j5+cm5tZ2ci7+H8N413kCIA/8J3B5IpddXezGRGRf4C7gMFXdIiKT8Q9M\njsc/jjEHuEdV9+qjzJcB+6nquyJSDYxT1fdFZArwNLA3/hPCjcDf4pf8WeCGoJa52nWAKNt/dXY1\n8K3snMR3gUXAP0JFnse8Ev8Elv8s8TWQjwHuUNUtAIViAvxRVfPAWhHZ3kSdh1S1+y1GAX4oIp/B\nf8LZDdgFOBy4W1VbgVYRubeE2UvOyjwCErnsVuCa7JzEtcAC4GTgRKJd7FV8VOCRvsxuW49/b+/g\nY88LI5wO7AzMV9UOEWkkhAstWplHUOH90icKHxdm5yRm4c8oOxF/FBjlMF4pZPEL/LsRmuTxCHCX\niPxYVd8p7GYPRwx4u1Dko4Hpha8/CdwgIlfgd+UE4JdFpy4TK7NDiVx2HXAVcFV2TmIy/rWxTgQW\nAju6zDZIW4EV+NMtf5/IZVeN5IOr6hoRuRz4k4h0AcO97MyvgXtFxMP/eXKF7S8XkXvw9zLeAjz8\nnzmQ7ABYAGXnJGrwd8fnAXPxz97aB7cH0bbhl2V5j48Xoz47S0QmqGqTiIzDP2PrLFUt6gh8uViZ\nQyI7JyHADPxiz+Wjks8Bakv4UG3AJmAjsIaPirs6kctG4v3YoRCR/8B/Ih0DLFHVwF7T2cocctk5\niVH4R193wB+5JwzwWfF3FXt+vIdf4E2JXHbEFjY0pWVlNiYibG62MRFhZTYmIqzMxkSEldmYiLAy\nGxMRVmZjIsLKbExEWJmNiQgrszERYWU2JiKszMZEhJXZmIiwMhsTEVZmYyLCymxMRFiZjYkIK7Mx\nEWFlNiYirMzGRISV2ZiIsDIbExFWZmMiwspsTERYmY2JCCuzMRFhZTYmIqzMxkSEldmYiLAyGxMR\nVmZjIsLKbExE/H8Bc6D0jU2uuAAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1FuszCyFHwEa",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}